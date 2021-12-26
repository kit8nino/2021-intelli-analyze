import pandas as pd

pd.options.mode.chained_assignment = None
data = pd.read_csv('../_lab-1/character-deaths.csv')
result = data[['Name', 'Gender']]
result['Name'] = result['Name'].str.partition(' ')[0]
result['Name'] = result['Name'].str.len()
correlation = result.corr()['Gender']['Name']
print('Correlation {}'.format(correlation))