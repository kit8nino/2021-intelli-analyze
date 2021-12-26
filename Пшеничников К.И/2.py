import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None
data = pd.read_csv('character-deaths.csv')

def task_g():
    dt = data[['Allegiances', 'Death Year']]
    dt = dt.drop(np.where(dt['Allegiances'] == 'None')[0])
    dt = dt.reset_index(drop=True)
    i = 0
    for x in dt['Allegiances']:
        dt['Allegiances'][i] = ord(x[0].lower()) - 96
        i += 1
    dt['Death Year'] = dt['Death Year'].fillna(dt['Death Year'].max())
    return np.corrcoef(dt['Death Year'].to_list(), dt['Allegiances'].to_list())[0, 1]

print('\n\nCтатистические данные по связи между номером первой буквы дома и годом смерти = '+str(task_g())+'\nЭто означает, что связь практически отсутствует')
