import numpy as np
import pandas as pd

# Variant 6

pd.options.mode.chained_assignment = None
data = pd.read_csv('../_lab-1/character-deaths.csv')


result = data[['Name', 'Allegiances']]
result['Name'] = result['Name'].str.partition(' ')[0].str.len()
result = result.drop(np.where(result['Allegiances'] == 'None')[0])
result['Allegiances'] = result['Allegiances'].str.len()
print("Result : {}".format(result.corr()['Name']['Allegiances']))