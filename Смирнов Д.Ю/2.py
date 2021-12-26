import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None
data = pd.read_csv('../_lab-1/character-deaths.csv')


def exercise():
    modified_data = data[['Allegiances', 'Death Year']]
    modified_data = modified_data.drop(np.where(modified_data['Allegiances'] == 'None')[0])
    modified_data = modified_data.reset_index(drop=True)
    i = 0
    for x in modified_data['Allegiances']:
        modified_data['Allegiances'][i] = ord(x[0].lower()) - 96
        i += 1
    modified_data['Death Year'] = modified_data['Death Year'].fillna(modified_data['Death Year'].max())
    return np.corrcoef(modified_data['Death Year'].to_list(), modified_data['Allegiances'].to_list())[0, 1]


print('Задание g ' + str(exercise()))
