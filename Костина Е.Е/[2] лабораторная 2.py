import pandas as pd
dt = pd.read_csv('../2021-intelli-analyze/_lab-1/character-deaths.csv')
dt_c = dt[['Death Year', 'Nobility']]
dt_c = dt_c.fillna(dt_c['Death Year'].mean())
c = dt_c.corr()['Death Year']['Nobility']
print('Анализ связи между годом смерти и благородностью')
if c > 0.1 :
    print('Cвязь между годом смерти и благородностью есть')
else :
    print('Cвязи между годом смерти и благородностью нет')
if c > 0 :
    print('Направление связи прямое')
else :
    print('Направление связи обратное')
print('Величина связи ', c)