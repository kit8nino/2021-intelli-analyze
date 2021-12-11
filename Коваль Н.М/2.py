import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None
data = pd.read_csv('../_lab-1/character-deaths.csv')


result = data[['Allegiances', 'Death Year']]
result = result.drop(np.where(result['Allegiances'] == 'None')[0])
result = result.reset_index(drop=True)
i = 0
for x in result['Allegiances']:
    result['Allegiances'][i] = ord(x[0].lower()) - 96
    i += 1
result['Death Year'] = result['Death Year'].fillna(result['Death Year'].max())
result = np.corrcoef(result['Death Year'].to_list(), result['Allegiances'].to_list())[0, 1]
print("Result {}".format(result))