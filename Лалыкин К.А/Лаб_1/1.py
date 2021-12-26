import numpy as np
import pandas as pd
import matplotlib as plt
import scipy

pd.options.mode.chained_assignment = None
data = pd.read_csv('../_lab-1/character-deaths.csv')

def exercise_c():
    data_c = data[['Death Year', 'Nobility']]
    data_c = data_c.fillna(data_c['Death Year'].mean())
    return data_c.corr()['Death Year']['Nobility']

print('Задание: \n\n с) '+ str(exercise_c()) + '\n ')
