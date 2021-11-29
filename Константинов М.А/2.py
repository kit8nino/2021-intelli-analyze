import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None

initial_data = pd.read_csv('../_lab-1/character-deaths.csv')
result = initial_data[['Allegiances', 'Death Chapter', 'Book Intro Chapter']]
result = result.drop(np.where(np.isnan(result['Death Chapter']))[0]).fillna(0)
result['Chapter Diff'] = result['Death Chapter'] - result['Book Intro Chapter']
result = result.drop(['Death Chapter', 'Book Intro Chapter'], axis=1).groupby('Allegiances').mean()
result = (result - result.min()) / (result.max() - result.min())
print(result)
