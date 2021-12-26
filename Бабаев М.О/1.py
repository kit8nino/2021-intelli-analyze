import numpy as np
import pandas as pd
import matplotlib as plt
import scipy

pd.options.mode.chained_assignment = None
data = pd.read_csv('../_lab-1/character-deaths.csv')

def isNaN(num):
    return num != num

def exercise_b():
    data_b = data[['Name', 'Gender']]
    data_b['Name'] = data_b['Name'].str.partition(' ')[0]
    data_b['Name'] = data_b['Name'].str.len()
    return data_b.corr()['Gender']['Name']

print('b) Cтатистические данные по связи между длиной имени и полом: ' + str(exercise_b()) + '\n ')

