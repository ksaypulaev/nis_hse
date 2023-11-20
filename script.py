import pandas as pd
# import numpy as np

plavki_df = pd.read_csv('plavki.csv', delimiter=',')
ostatki_df = pd.read_csv('ostatki.csv', delimiter=',')
try:
    '''col_C_list = plavki_df['C'].tolist()
    col_Si_list = plavki_df['Si'].tolist()
    col_Mn_list = plavki_df['Mn'].tolist()
    col_S_list = plavki_df['S'].tolist()
    col_P_list = plavki_df['P'].tolist()
    col_Al_list = plavki_df['Al'].tolist()
    col_Cr_list = plavki_df['Cr'].tolist()
    col_Ni_list = plavki_df['Ni'].tolist()
    col_Cu_list = plavki_df['Cu'].tolist()
    col_N_list = plavki_df['N'].tolist()
    col_Ti_list = plavki_df['Ti'].tolist()
    col_Nb_list = plavki_df['Nb'].tolist()
    col_Sn_list = plavki_df['Sn'].tolist()
    col_V_list = plavki_df['V'].tolist()
    col_B_list = plavki_df['B'].tolist()
    col_Mo_list = plavki_df['Mo'].tolist()
    col_Ca_list = plavki_df['Ca'].tolist()'''

    MS_1_condition = (
        (plavki_df['Cr'] + plavki_df['Ni'] + plavki_df['Cu'] <= 0.9) & 
        (plavki_df['Cr'] <= 0.25) & 
        (plavki_df['Ni'] <= 0.4) & 
        (plavki_df['Cu'] <= 0.25)
    )
    
    MS_2_condition = (
        (plavki_df['Cr'] + plavki_df['Ni'] + plavki_df['Cu'] < 0.9) & 
        (plavki_df['S'] < 0.08)
    )

    MS_3_condition = (
        (plavki_df['Cr'] + plavki_df['Ni'] + plavki_df['Cu'] < 0.9) & 
        (plavki_df['Cr'] < 0.25) & 
        (plavki_df['Ni'] < 0.4) & 
        (plavki_df['Cu'] < 0.25)
    )
    print(f'{MS_1_condition}\n\n{MS_2_condition}')
except Exception as ex:
    print(f'An exception occured: {ex}')
else:
    print("\nThe program finished successfuly!")
