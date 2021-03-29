import pandas as pd

xlsx = pd.ExcelFile('C:\\Users\\Daeron\\PycharmProjects\\DataBase\\CatDogs.xlsx')

ex_data = pd.read_excel('CatDogs.xlsx', [0, 1, 2])

print('Cats median', ex_data[0]['Cats weight'].median(axis=0))
print('Dogs median', ex_data[1]['Dogs weight'].median(axis=0))
print('Huma median', ex_data[2]['Humans weight'].median(axis=0))
print('Cats arg', ex_data[0]['Cats weight'].mean(axis=0))
print('Dogs arg', ex_data[1]['Dogs weight'].mean(axis=0))
print('Huma arg', ex_data[2]['Humans weight'].mean(axis=0))
