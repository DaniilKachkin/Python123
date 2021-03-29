import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('C:\\Users\\Daeron\\PycharmProjects\\DataBase\\USA_Dollar.xlsx')
xls = pd.ExcelFile('C:\\Users\\Daeron\\PycharmProjects\\DataBase\\Oil.xls')
Dollar = pd.read_excel('USA_Dollar.xlsx', [0])
Oil = pd.read_excel('Oil.xls', [1], skiprows=2,
                    names=['Date', 'Oil_price'])  # - скип первых двух колонок и переименование последующих
# print(Dollar)
# print(Oil)
# print(Dollar[0]['curs'].plot())  # - грфик курса доллара
# print(Oil[1]['Oil_price'].plot())
# plt.show()

Gluing = Dollar[0].set_index('Date').join(Oil[1].set_index('Date'))  # - объединение двух таблиц по дате
# print(Gluing)
Gluing.drop(['Nominal', 'Cdx'], axis=1, inplace=True)  # - выкидываем лишние колонки и даём запомнить (inplace)
# print(Gluing)
Gluing.fillna(method='ffill', inplace=True)  # - заменяем NA (fillna) на значения предыдущего дня (ffill)
# print(Gluing)
Gluing.reset_index(inplace=True)  # - обновляем левый столбец нумерации по порядку после изменений
# print(Gluing)
# plt.plot(Gluing['Date'], Gluing['Curs'], label = 'USD/RUB Rate') # - строим график по нужным пенременным + легенда
# plt.plot(Gluing['Date'], Gluing['Oil_price'], label = 'Oil Price')
# plt.legend() # - команда вывести легенду
# plt.show() # - выводим график вместе с легендой
Gluing['Year'] = Gluing['Date'].dt.year  # - создаём год
Gluing['Month'] = Gluing['Date'].dt.month
Gluing['Weekday'] = Gluing['Date'].dt.weekday
# print(Gluing)
past_days = 7  # - статистика за 7 дней в прошлом
for day in range(past_days):
    d = day + 1
    Gluing[f'USD_back_{d}d'] = Gluing['Curs'].shift(d)
    Gluing[f'Oil_back_{d}d'] = Gluing['Oil_price'].shift(d)
# print(Gluing)
# print(Gluing.tail(7)) # - вывод последних N строк
Gluing['USD_median'] = Gluing['Curs'].shift(1).rolling(window=7).median()  # - создание медиваны за неделю для доллара
Gluing['Oil_median'] = Gluing['Oil_price'].shift(1).rolling(
    window=7).median()  # - создание медиваны за неделю для нефти
# print(Gluing.shape) # - вывод кол-ва строк и столбцов в таблице
Gluing = pd.get_dummies(Gluing, columns=['Year', 'Month', 'Weekday'])  # - кодируем столбцы в бинарные
Gluing.drop(['Date', 'Oil_price'], axis=1, inplace=True)  # - удаляем лишние столбцы, из которых выжали всю информацию
Gluing.dropna(inplace=True)  # - выкидываем все оставшиеся NA
x = Gluing.drop('Curs', axis=1)  # - создание независимой переменной
y = Gluing['Curs']  # - создание зависимой переменной
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33)  # создание тренировочной и обучающей ваыборок
from sklearn.linear_model import LinearRegression

Regression = LinearRegression()
Regression.fit(x_train, y_train)
# Prediction = Regression.predict(x_test)
# print(Prediction)
# print(y_test)

#from sklearn.ensemble import RandomForestRegressor
#model = RandomForestRegressor() # - random_state
#model = gs.best_estimator_
#model.fit(x_train, y_train)
#Prediction = model.predict(x_test)
from sklearn.metrics import mean_absolute_error
# print(mean_absolute_error(y_test, Prediction))
from sklearn.metrics import max_error
# print(max_error(y_test, Prediction))

from sklearn.neighbors import KNeighborsRegressor

# model = KNeighborsRegressor()
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [5, 100],
    'criterion': ['mse', 'mae'],
    'max_depth': [3, 15]
}
gs = GridSearchCV(model, param_grid, 'neg_mean_absolute_error', cv=3)
gs.fit(x_train, y_train)
model = gs.best_estimator_
Prediction = model.predict(x_test)
print(gs.best_score_)
print(gs.best_params_)
print(gs.best_estimator_)

model.fit(x_train, y_train)

from sklearn.metrics import mean_absolute_error
print(mean_absolute_error(y_test, Prediction))
from sklearn.metrics import max_error
print(max_error(y_test, Prediction))
