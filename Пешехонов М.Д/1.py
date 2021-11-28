import numpy as np
import pandas as pd


# Пешехонов М. Д. гр.ИС-27
# Вариант 'e'
# Проанализировать и выдать статистические данные по связи между:
#   e) благородностью и номером первой буквы имени (A -1, B -2 и т.д)

def execute_task(data):
    i = 0
    for x in data['Name']:
        data['Name'][i] = ord(x[0].lower()) - 96
        i += 1
    return np.corrcoef(data['Name'].to_list(), data['Nobility'].to_list())[0, 1]


if __name__ == '__main__':
    pd.options.mode.chained_assignment = None
    df = pd.read_csv('../_lab-1/character-deaths.csv')
    corr = execute_task(df[['Name', 'Nobility']])
    print(f"Связь имеется и её велечина = {corr}")
    if corr > 0:
        print("Прямая связь между благородностью и номером первой буквы имени")
    else:
        print("Обратная связь между благородностью и номером первой буквы имени")