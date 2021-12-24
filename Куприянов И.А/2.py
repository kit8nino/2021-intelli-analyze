import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None
data = pd.read_csv('../_lab-1/character-deaths.csv')


def task():
    selected_columns = data[['Book of Death', 'Allegiances']]
    selected_columns = selected_columns.fillna(1)
    selected_columns = selected_columns.drop(np.where(selected_columns['Allegiances'] == 'None')[0])
    selected_columns['Allegiances'] = selected_columns['Allegiances'].str.len()
    return selected_columns.corr()['Book of Death']['Allegiances']


print('Задание D  ' + str(task()))

