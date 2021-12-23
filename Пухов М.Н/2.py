import numpy as np
import pandas as pd
import matplotlib as plt
import scipy

pd.options.mode.chained_assignment = None
data = pd.read_csv('../_lab-1/character-deaths.csv')


def isNaN(num):
    return num != num


def exercise_a():
    data_a = data[['Allegiances', 'Death Chapter', 'Book Intro Chapter']]
    data_a = data_a.drop(np.where(isNaN(data['Death Chapter']))[0]).fillna(0)
    data_a['Chapter Diff'] = data_a['Death Chapter'] - data_a['Book Intro Chapter']
    data_a = data_a.drop(['Death Chapter', 'Book Intro Chapter'], axis=1).groupby('Allegiances').mean()
    data_a = (data_a - data_a.min()) / (data_a.max() - data_a.min())
    return data_a

print('Задания: \n\n a) ' + str(exercise_a()) + '\n ')
                   
