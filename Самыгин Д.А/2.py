import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None
data = pd.read_csv('E:/character-deaths.csv')

def exercise_d():
    data_d = data[['Book of Death', 'Allegiances']]
    data_d = data_d.fillna(1)
    data_d = data_d.drop(np.where(data_d['Allegiances'] == 'None')[0])
    data_d['Allegiances'] = data_d['Allegiances'].str.len()
    return data_d.corr()['Book of Death']['Allegiances']

print('Задание: \n\n  d) ' + str(exercise_d()) + '\n\n Зависимости между Книгой смерти и названием дома нету')