import tkinter as tk
import pandas as pd


try:
    plavki_df = pd.read_csv('plavki.csv', delimiter=',')
    ostatki_df = pd.read_csv('ostatki.csv', delimiter=',')
    plavki_df_str = plavki_df.to_string()
    ostatki_df_str = ostatki_df.to_string()

    def read_tables():
        result_label.config(text="Execution successful!")
        text_content.delete(1.0, tk.END)  # Clear previous content
        text_content.insert(tk.END, "Plavki Data:\n\n")
        text_content.insert(tk.END, plavki_df_str)
        text_content.insert(tk.END, "\n\nOstatki Data:\n\n")
        text_content.insert(tk.END, ostatki_df_str)

    def execute_script():
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

        for ms in MS_1_condition:
            if ms:
                take_lom_1_MS_1 = 60 * 1
                take_scrap_MS_1 = 5
                #output += 'True!\n'
                pass
            else:
                #output += 'False!\n'
                pass

        for ms in MS_2_condition:
            if ms:
                take_lom_1_MS_2 = 60 * 0.4
                take_shd_lom_MS_2 = 60 * 0.6
                #output += 'True!\n'
                pass
            else:
                #output += 'False!\n'
                pass

        for ms in MS_3_condition:
            if ms:
                take_lom_2_MS_3 = 60 * 0.55
                take_chugun_MS_3 = 60 * 0.45
                #output += 'True!\n'
                pass
            else:
                #output += 'False!\n'
                pass

        take_total_lom_1 = take_lom_1_MS_1 + take_lom_1_MS_2
        take_total_lom_2 = take_lom_2_MS_3
        take_total_shd_lom = take_shd_lom_MS_2
        take_total_chugun = take_chugun_MS_3
        text_content.insert(tk.END, '\n\n')
        text_content.insert(tk.END, f'Итого заказать лома 1 сорта: {take_total_lom_1}')
        text_content.insert(tk.END, '\n')
        text_content.insert(tk.END, f'Итого заказать лома 2 сорта: {take_total_lom_2}')
        text_content.insert(tk.END, '\n')
        text_content.insert(tk.END, f'Итого заказать легированного лома: {take_total_shd_lom}')
        text_content.insert(tk.END, '\n')
        text_content.insert(tk.END, f'Итого заказать чугунного лома: {take_total_chugun}')
   
    def reading():
        read_tables()
        execute_script()
        print("Data updated!")

    # Create the main window
    root = tk.Tk()
    root.title("Test script GUI")

    # Set a fixed window size (width x height)
    root.geometry("1000x450")  # Change width and height as needed

    # Button to execute the script
    update_button = tk.Button(root, text="Get data!", command=reading, width=20, height=2)
    update_button.pack(side=tk.TOP, pady=10)

    update_button = tk.Button(root, text="Update data!", command=reading, width=20, height=2)
    update_button.pack(side=tk.TOP, pady=10)

    # Label to display the script's result
    result_label = tk.Label(root, text="", justify="left", anchor="w", wraplength=480)
    result_label.pack()

    # Text widget to display plavki_df and ostatki_df
    text_content = tk.Text(root, wrap="word")
    text_content.pack(fill="both", expand=True)

except Exception as ex:
    result_label.config(text=f"An exception occurred: {ex}")

# Run the GUI application
root.mainloop()
