import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None
data = pd.read_csv('character-deaths.csv')

def zad_g():
    data_g = data[['Allegiances', 'Death Year']]
    data_g = data_g.drop(np.where(data_g['Allegiances'] == 'None')[0])
    data_g = data_g.reset_index(drop=True)
    i = 0
    for x in data_g['Allegiances']:
        data_g['Allegiances'][i] = ord(x[0].lower()) - 96
        i += 1
    data_g['Death Year'] = data_g['Death Year'].fillna(data_g['Death Year'].max())
    return np.corrcoef(data_g['Death Year'].to_list(), data_g['Allegiances'].to_list())[0, 1]


print('Зависимости между номером первой буквы дома и годом смерти нет \n\n' + str(zad_g()) + '\n ')
