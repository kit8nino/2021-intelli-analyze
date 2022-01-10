import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/manin/OneDrive/Documents/GitHub/2021-intelli-analyze/Манин К.А/character-deaths.csv")

print("Манин Кирилл ИС-27")
print("Лабораторная работа №1\nОценка взаимосвязей, корреляция")
print("Задание а")
print("Проанализировать и выдать статистические данные связи между:\n"
      "Домом и разницей в главах")

data = data[['Allegiances', 'Death Chapter', 'Book Intro Chapter']]
data = data.drop(np.where(np.isnan(data['Death Chapter']))[0]).fillna(0)
data['Chapter diff'] = data['Death Chapter'] - data['Book Intro Chapter']
data = data.drop(['Death Chapter', 'Book Intro Chapter'], axis=1).groupby('Allegiances').mean()
data = (data - data.min()) / (data.max() - data.min())

print("Результат: " + str(data)) 
