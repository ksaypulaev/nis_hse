import pandas as pd
# import numpy as np

plavki = pd.read_csv('plavki.csv', delimiter=',')
ostatki = pd.read_csv('ostatki.csv', delimiter=',')
try:
    print(f"{plavki}")
    print('-' * 100)
    print(ostatki)
except Exception as ex:
    print(f'An exception occured: {ex}')
else:
    print("\nThe program finished successfuly!")
