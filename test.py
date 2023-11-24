import tkinter as tk
import pandas as pd


try:
    # вывод исходных таблиц
    def print_tables():
        plavki_df = pd.read_csv('plavki.csv', delimiter=',')
        ostatki_df = pd.read_csv('ostatki.csv', delimiter=',')
        plavki_df_str = plavki_df.to_string()
        ostatki_df_str = ostatki_df.to_string()
        result_label.config(text="Execution successful!")
        text_content.delete(1.0, tk.END)  # Clear previous content
        text_content.insert(tk.END, "Plavki Data:\n\n")
        text_content.insert(tk.END, plavki_df_str)
        text_content.insert(tk.END, "\n\nOstatki Data:\n\n")
        text_content.insert(tk.END, ostatki_df_str)

    # проверка марок стали и расчет/вывод итогового заказа и баланса остатков
    def execute_script():
        plavki_df = pd.read_csv('plavki.csv', delimiter=',')
        ostatki_df = pd.read_csv('ostatki.csv', delimiter=',')
        plavki_df_str = plavki_df.to_string()
        ostatki_df_str = ostatki_df.to_string()

        # условия марок стали
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
        
        # Create a string to store the output
        output = ""

        # расчеты требуемых материалов для каждой марки стали
        ms_1_count = 0
        for ms in MS_1_condition:
            if ms:
                ms_1_count += 1
                take_lom_1_MS_1 = 60 * 1 * ms_1_count
                take_scrap_MS_1 = 5 * ms_1_count
                #output += 'True!\n'
                pass
            else:
                #output += 'False!\n'
                pass
        
        ms_2_count = 0
        for ms in MS_2_condition:
            if ms:
                ms_2_count += 1
                take_lom_1_MS_2 = 60 * 0.4 * ms_2_count
                take_shd_lom_MS_2 = 60 * 0.6 * ms_2_count
                #output += 'True!\n'
                pass
            else:
                #output += 'False!\n'
                pass

        ms_3_count = 0
        for ms in MS_3_condition:
            if ms:
                ms_3_count += 1
                take_lom_2_MS_3 = 60 * 0.55 * ms_3_count
                take_chugun_MS_3 = 60 * 0.45 * ms_3_count
                #output += 'True!\n'
                pass
            else:
                #output += 'False!\n'
                pass
        
        # суммирование материалов лома для единого заказа
        take_total_lom_1 = take_lom_1_MS_1 + take_lom_1_MS_2
        take_total_lom_2 = take_lom_2_MS_3
        take_total_shd_lom = take_shd_lom_MS_2
        take_total_chugun = take_chugun_MS_3
        take_total_scrap = take_scrap_MS_1

        # вычитание итогов из остатков 
        ost_lom_1 = max(0, ostatki_df.loc[ostatki_df['name'] == 'лом 1 сорт', 'as_is_ost'].values[0] - take_total_lom_1)
        ost_lom_2 = max(0, ostatki_df.loc[ostatki_df['name'] == 'лом 2 сорт', 'as_is_ost'].values[0] - take_total_lom_2)
        ost_shd_lom = max(0, ostatki_df.loc[ostatki_df['name'] == 'лом легированный', 'as_is_ost'].values[0] - take_total_shd_lom)
        ost_chugun = max(0, ostatki_df.loc[ostatki_df['name'] == 'чугун', 'as_is_ost'].values[0] - take_total_chugun)
        ost_scrap = max(0, ostatki_df.loc[ostatki_df['name'] == 'скрап', 'as_is_ost'].values[0] - take_total_scrap)

        # расчет количества материалов, необходимых для дозаказа после вычета из остатков
        additional_lom_1 = abs(min(0, ostatki_df.loc[ostatki_df['name'] == 'лом 1 сорт', 'as_is_ost'].values[0] - take_total_lom_1))
        additional_lom_2 = abs(min(0, ostatki_df.loc[ostatki_df['name'] == 'лом 2 сорт', 'as_is_ost'].values[0] - take_total_lom_2))
        additional_shd_lom = abs(min(0, ostatki_df.loc[ostatki_df['name'] == 'лом легированный', 'as_is_ost'].values[0] - take_total_shd_lom))
        additional_chugun = abs(min(0, ostatki_df.loc[ostatki_df['name'] == 'чугун', 'as_is_ost'].values[0] - take_total_chugun))
        additional_scrap = abs(min(0, ostatki_df.loc[ostatki_df['name'] == 'скрап', 'as_is_ost'].values[0] - take_total_scrap))

        # вывод данных в GUI приложение
        text_content.insert(tk.END, '\n\n\n')
        text_content.insert(tk.END, '---------------------------------------------------------------------------------------------------------------------------------------------')
        text_content.insert(tk.END, f'Итого требуется лома 1 сорта: {take_total_lom_1}, Баланс остатков: {ost_lom_1}, Необходимо дозаказать: {additional_lom_1}')
        text_content.insert(tk.END, '\n\n')
        text_content.insert(tk.END, f'Итого требуется лома 2 сорта: {take_total_lom_2}, Баланс остатков: {ost_lom_2}, Необходимо дозаказать: {additional_lom_2}')
        text_content.insert(tk.END, '\n\n')
        text_content.insert(tk.END, f'Итого требуется легированного лома: {take_total_shd_lom}, Баланс остатков: {ost_shd_lom}, Необходимо дозаказать: {additional_shd_lom}')
        text_content.insert(tk.END, '\n\n')
        text_content.insert(tk.END, f'Итого требуется чугунного лома: {take_total_chugun}, Баланс остатков: {ost_chugun}, Необходимо дозаказать: {additional_chugun}')
        text_content.insert(tk.END, '\n\n')
        text_content.insert(tk.END, f'Итого требуется скрапа: {take_total_scrap}, Баланс остатков: {ost_scrap}, Необходимо дозаказать: {additional_scrap}')

    # выполнение всех скриптов и вывод лога обновления данных в консоль
    def execute():
        print_tables()
        execute_script()
        print("Data updated!")

    # Create the main window
    root = tk.Tk()
    root.title("Test script GUI")

    # Set a fixed window size (width x height)
    root.geometry("1000x650")  # Change width and height as needed

    # Button to execute the script
    update_button = tk.Button(root, text="Get data!", command=execute, width=20, height=2)
    update_button.pack(side=tk.TOP, pady=10)

    # Button to update the script
    update_button = tk.Button(root, text="Update data!", command=execute, width=20, height=2)
    update_button.pack(side=tk.TOP, pady=10)

    # Label to display the script's result
    result_label = tk.Label(root, text="", justify="left", anchor="w", wraplength=480)
    result_label.pack()

    # Text widget to display plavki_df and ostatki_df
    text_content = tk.Text(root, wrap="word")
    text_content.pack(fill="both", expand=True)

# обработка исключений
except Exception as ex:
    result_label.config(text=f"An exception occurred: {ex}")

# Run the GUI application
root.mainloop()
