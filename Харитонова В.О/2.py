import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None
data = pd.read_csv('D:/1/character-deaths.csv')

def var_g():
    dt = data[['Allegiances', 'Death Year']]
    dt = dt.drop(np.where(dt['Allegiances'] == 'None')[0])
    dt = dt.reset_index(drop=True)
    i = 0
    for x in dt['Allegiances']:
        dt['Allegiances'][i] = ord(x[0]) - 64
        i += 1
    dt['Death Year'] = dt['Death Year'].fillna(dt['Death Year'].max())
    return np.corrcoef(dt['Death Year'].to_list(), dt['Allegiances'].to_list())[0, 1]
print('Вариант g: Проанализировать и выдать статистические данные по связи между ' +
'номером первой буквы дома и годом смерти'
'\n Выполнила Харитонова В.О. \n')
print('Ответ: ' + str(var_g()) + '\n Обратная связь, практически отсутствует')