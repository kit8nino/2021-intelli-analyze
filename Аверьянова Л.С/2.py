import numpy as np
import pandas as pd
import matplotlib as plt
import scipy

pd.options.mode.chained_assignment = None
data = pd.read_csv('../_lab-1/character-deaths.csv')

def exercise_f():
    data_f = data[['Name', 'Allegiances']]
    data_f['Name'] = data_f['Name'].str.partition(' ')[0]
    data_f['Name'] = data_f['Name'].str.len()
    data_f = data_f.drop(np.where(data_f['Allegiances'] == 'None')[0])
    data_f['Allegiances'] = data_f['Allegiances'].str.len()
    return data_f.corr()['Name']['Allegiances']


print('Задание: \n\n f) ') + str(exercise_f()) + '\n ')
