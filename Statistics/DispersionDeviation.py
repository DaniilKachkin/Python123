import pandas as pd

xlsx = pd.ExcelFile('C:\\Users\\Daeron\\PycharmProjects\\DataBase\\CatDogs.xlsx')

ex_data = pd.read_excel('CatDogs.xlsx', [0, 1, 2])

print(ex_data[0]['Cats weight'].mad(axis=0)) # mean absolute deviation
print(ex_data[0]['Cats weight'].std(axis=0))  # standart deviation (среднеквадратическое отклонение)
# print(ex_data[0]['Cats weight'].describe(axis=0)) # а где дисперсия?

