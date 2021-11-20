import numpy as np
import pandas as pd
import matplotlib as plt
import scipy

pd.options.mode.chained_assignment = None
data = pd.read_csv('../_lab-1/character-deaths.csv')


# data_droppedA2.describe()

def isNaN(num):
    return num != num


# print(data.drop(np.where(isNaN(data['Death Chapter']))[0]).fillna(0))


def exercise_a():
    data_a = data[['Allegiances', 'Death Chapter', 'Book Intro Chapter']]
    data_a = data_a.drop(np.where(isNaN(data['Death Chapter']))[0]).fillna(0)
    data_a['Chapter Diff'] = data_a['Death Chapter'] - data_a['Book Intro Chapter']
    data_a = data_a.drop(['Death Chapter', 'Book Intro Chapter'], axis=1).groupby('Allegiances').mean()
    data_a = (data_a - data_a.min()) / (data_a.max() - data_a.min())
    return data_a


def exercise_b():
    data_b = data[['Name', 'Gender']]
    data_b['Name'] = data_b['Name'].str.partition(' ')[0]
    data_b['Name'] = data_b['Name'].str.len()
    return data_b.corr()['Gender']['Name']


def exercise_c():
    data_c = data[['Death Year', 'Nobility']]
    data_c = data_c.fillna(data_c['Death Year'].mean())
    return data_c.corr()['Death Year']['Nobility']


def exercise_d():
    data_d = data[['Book of Death', 'Allegiances']]
    data_d = data_d.fillna(1)
    data_d = data_d.drop(np.where(data_d['Allegiances'] == 'None')[0])
    data_d['Allegiances'] = data_d['Allegiances'].str.len()
    return data_d.corr()['Book of Death']['Allegiances']


def exercise_e():
    data_e = data[['Name', 'Nobility']]
    i = 0
    for x in data_e['Name']:
        data_e['Name'][i] = ord(x[0].lower()) - 96
        i += 1
    return np.corrcoef(data_e['Name'].to_list(), data_e['Nobility'].to_list())[0, 1]


def exercise_f():
    data_f = data[['Name', 'Allegiances']]
    data_f['Name'] = data_f['Name'].str.partition(' ')[0]
    data_f['Name'] = data_f['Name'].str.len()
    data_f = data_f.drop(np.where(data_f['Allegiances'] == 'None')[0])
    data_f['Allegiances'] = data_f['Allegiances'].str.len()
    return data_f.corr()['Name']['Allegiances']


def exercise_g():
    data_g = data[['Allegiances', 'Death Year']]
    data_g = data_g.drop(np.where(data_g['Allegiances'] == 'None')[0])
    data_g = data_g.reset_index(drop=True)
    i = 0
    for x in data_g['Allegiances']:
        data_g['Allegiances'][i] = ord(x[0].lower()) - 96
        i += 1
    data_g['Death Year'] = data_g['Death Year'].fillna(data_g['Death Year'].max())
    return np.corrcoef(data_g['Death Year'].to_list(), data_g['Allegiances'].to_list())[0, 1]


print('Задания: \n\n a) ' + str(exercise_a()) + '\n '
                      'b) ' + str(exercise_b()) + '\n '
                      'c) ' + str(exercise_c()) + '\n '
                      'd) ' + str(exercise_d()) + '\n '
                      'e) ' + str(exercise_e()) + '\n '
                      'f) ' + str(exercise_f()) + '\n '
                      'g) ' + str(exercise_g()) + '\n ')
