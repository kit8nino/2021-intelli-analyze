import pandas as pd
import numpy as np
dt=pd.read_csv('D:/work/2021-intelli-analyze/_lab-1/character-deaths.csv')

# Вступление
print("\nАнализ выполнила студентка группы ИС-27 Куприянова Татьяна")
print("Вариант задания - 11. Дом Грейджоев - House Greyjoy")

# Анализ связей
print("\nАнализ связей между домом и разницей в главах")
print("в которой появился и в которой умер")
dt = dt[['Allegiances', 'Death Chapter', 'Book Intro Chapter']]
dt = dt.drop(np.where(np.isnan(dt['Death Chapter']))[0]).fillna(0)
dt['Chapter diff'] = dt['Death Chapter'] - dt['Book Intro Chapter']
dt = dt.drop(['Death Chapter', 'Book Intro Chapter'], axis=1).groupby('Allegiances').mean()
dt = (dt - dt.min()) / (dt.max() - dt.min())
print(str(dt))

# Общая статистика
print("\nОбщая статистика смертей в каждом доме")
dt['Allegiances'].value_counts(normalize=True)
print("\nИсходя из выведенной информации Дом Грейджоев находится на десятом месте")
print("по числу людей,в чьем доме чаще умирали")

# Вывод всех людей из Дома Грейджоев
print("\nСтатистика всех людей из Дома Грейджоев")
dt[dt['Allegiances'].isin(['House Greyjoy'])]
print("\nИсходя из выведенной информации в Доме Грейджоев было 24 человека")

# Gender - Пол	
print("\nОбщая статистика гендерной принадлежности в каждом доме")
dt.groupby('Gender').Allegiances.value_counts()
print("\nИсходя из выведенной информации в Доме Грейджоев")
print("численнось состоит из 1 женщины и 23 мужчин. Итого 24 человека\n")

dt.groupby('Gender').Allegiances.value_counts(normalize=True)
print("\nВ процентном соотношении получается")
print("0.006369 женщин и 0.030263 мужчин")

# Death Year - Год смерти
print("\nОбщая статистика в каком доме и в каком году сколько людей умерло")
dt.groupby('Death Year').Allegiances.value_counts()
print("\nИсходя из выведенной информации в Доме Грейджоев")
print("в 297 и 298 годах никто не умер")
print("в 299 году умерло 11 человек, в 300 году умело 3 человека")
print("Итого умерло 14 человек")

# Nobility - Благородство
print("\nОбщая статистика в каком доме и сколько было благородных людей")
dt.groupby('Allegiances').Nobility.value_counts()
print("\nИсходя из выведенной информации в Доме Грейджоев")
print("было 19 благородных женщин")
print("и 5 благородных мужчин")

# Сортировка по алфавиту
print("\nОбщая статистика, на каком месте каждый дом при алфавитной сортировки")
dt['Allegiances'].value_counts().sort_index(ascending=True)
print("\nИсходя из выведенной информации Дом Грейджоев")
print("на 6 месте в алфавитном порядке")

# Общая Корреляция
print("\nОбщая статистика с корреляцией")
dt.corr()

# Корреляция по столбцам
print("\nКорреляция по году смерти и книге смерти")
dt['Death Year'].corr(dt['Book of Death'])

print("\nКорреляция по полу и главе вступления в книге")
dt['Gender'].corr(dt['Book Intro Chapter'])

# Вывод
print("\nТаким образом, был проведен анализ данных из таблицы. Можно прийти к следующему выводу:")
print("Из 24 человек умерло 14, а значит в живых осталось лишь 10 человек.")
print("Количество людей из Дома Грейджоев сократилось примерно в 1,7 раз")