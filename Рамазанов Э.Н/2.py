import numpy as np
import pandas as pd


data = pd.read_csv('character-deaths.csv')

def zadanie_d():
    data_d = data[['Book of Death', 'Allegiances']]
    data_d = data_d.fillna(1)
    data_d = data_d.drop(np.where(data_d['Allegiances'] == 'None')[0])
    data_d['Allegiances'] = data_d['Allegiances'].str.len()
    Corr = data_d.corr()['Book of Death']['Allegiances']
    if Corr > 0:
        print ('Прямая связь')
    else:
        print ('Обратная связь')
    print (Corr)
    return 0

print('Ramazanov Elshan\n' + 'Задание d\n')
zadanie_d()