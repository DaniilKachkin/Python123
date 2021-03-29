import pandas
import pandas as pd
import matplotlib.pyplot as plt
xlsx = pd.ExcelFile('C:\\Users\\Daeron\\PycharmProjects\\DataBase\\CatDogs.xlsx')

weight = pd.read_excel('CatDogs.xlsx', [0, 1, 2])
# print(weight[0].shape) # - вывод количества строк и колонок
# print(weight[0].head(3)) # - вывести первые четыре колонки
# print(weight[0]['Cats weight']) # -показать столбец вес кошек - работает
# print(weight[0]['Cats weight'].describe()) # - вывести статистику данной колонки
# print(weight[0]['Cats weight'].hist()) # - показывает диаграмму веса котов
# plt.show() # - показывает диаграмму веса котов
# print(weight[0][weight[0]['Cats weight'] == 5])  # - показывает кол-во котов с весом в 5 кг
# print(weight[0]['Color'].value_counts()) # - показывает количество котов каждого цвета

# print(weight[0]['Color'].value_counts().plot(kind='bar')) # - столбчатая диаграмма котов каждого цвета
# plt.show() # - птолбчатая диаграмма котов каждого цвета

# pandas.get_dummies(weight[0], columns=['Color']) # - создание многих колонок по цветам

final_df = pandas.get_dummies(weight[0], columns=['Color']) # - вывод всей изменённой таблицы
# print(final_df) # - вывод всей изменённой таблицы

x = final_df.drop('Species', axis=1) # - выбор всего, кроме колонки с породой
y = final_df['Species'] # - выбор только породы
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
(model.fit(x, y)) # - это машинное обучение
{ col:[0] for col in x.columns}
example = {'Cats weight': [5], # - достать из дебага
           'Color_Black': [0], # - достать из дебага
           'Color_Brown': [0], # - достать из дебага
           'Color_Grey': [0], # - достать из дебага
           'Color_Red': [1], # - достать из дебага
           'Color_White': [0]} # - достать из дебага
example_df = pandas.DataFrame(example)
print(model.predict(example_df)) # - создание предсказания
