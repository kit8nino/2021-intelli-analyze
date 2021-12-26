import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None
data = pd.read_csv('..\lab\character-deaths.csv')

def exercise_b():
    data_b = data[['Name', 'Gender']]
    data_b['Name'] = data_b['Name'].str.partition(' ')[0]
    data_b['Name'] = data_b['Name'].str.len()
    return data_b.corr()['Gender']['Name']
print('Связи между длиной имени и полом: \n\n b) ' + str(exercise_b()) + '\n ')
