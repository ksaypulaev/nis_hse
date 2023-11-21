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

    print(f'\n{ostatki_df}\n')

    MS_1_condition = (
        (plavki_df['Cr'] + plavki_df['Ni'] + plavki_df['Cu'] <= 0.9) & 
        (plavki_df['Cr'] <= 0.25) & 
        (plavki_df['Ni'] <= 0.4) & 
        (plavki_df['Cu'] <= 0.25)
    )

    MS_2_condition = (
        (plavki_df['Cr'] + plavki_df['Ni'] + plavki_df['Cu'] <= 0.9) & 
        (plavki_df['S'] <= 0.08)
    )

    MS_3_condition = (
        (plavki_df['C'] + plavki_df['Si'] + plavki_df['Mn'] <= 0.45) &
        (plavki_df['C'] <= 0.2) &
        (plavki_df['Si'] <= 0.1) &
        (plavki_df['Mn'] <= 0.4)
    )

    for ms in MS_1_condition:
        if ms:
            take_lom_1_MS_1 = 60 * 1
            take_scrap_MS_1 = 5
            #print(ostatki_df['лом 1 сорт', 'as_is_ost'] - take_lom_1_MS_1)
            print('True!')
        else:
            print('False!')

    for ms in MS_2_condition:
        if ms:
            take_lom_1_MS_2 = 60 * 0.4
            take_shd_lom_MS_2 = 60 * 0.6
            print('True!')
        else:
            print('False!')

    for ms in MS_3_condition:
        if ms:
            take_lom_2_MS_3 = 60 * 0.55
            take_chugun_MS_3 = 60 * 0.45
            print('True!')
        else:
            print('False!')

    #print(f'{MS_1_condition}\n\n{MS_2_condition}\n\n{MS_3_condition}')
except Exception as ex:
    print(f'An exception occured: {ex}')
else:
    print("\n\nThe program finished successfuly!")
