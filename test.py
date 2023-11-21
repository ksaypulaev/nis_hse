import tkinter as tk
import pandas as pd

def execute_script():
    try:
        plavki_df = pd.read_csv('plavki.csv', delimiter=',')
        ostatki_df = pd.read_csv('ostatki.csv', delimiter=',')

        # Convert dataframes to strings
        plavki_df_str = plavki_df.to_string()
        ostatki_df_str = ostatki_df.to_string()

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

        # Update the label with the output and DataFrame strings
        result_label.config(text="Execution successful!")
        
        # Clear previous content in the Text widget and insert new data
        text_content.delete(1.0, tk.END)  # Clear previous content
        text_content.insert(tk.END, "Plavki Data:\n\n")
        text_content.insert(tk.END, plavki_df_str)
        text_content.insert(tk.END, "\n\nOstatki Data:\n\n")
        text_content.insert(tk.END, ostatki_df_str)
        
    except Exception as ex:
        result_label.config(text=f"An exception occurred: {ex}")

def update_content():
    execute_script()

# Create the main window
root = tk.Tk()
root.title("Script GUI")

# Set a fixed window size (width x height)
root.geometry("1000x450")  # Change width and height as needed

# Button to execute the script
update_button = tk.Button(root, text="Update data!", command=update_content, width=20, height=2)
update_button.pack(pady=20)

# Label to display the script's result
result_label = tk.Label(root, text="", justify="left", anchor="w", wraplength=480)
result_label.pack()

# Text widget to display plavki_df and ostatki_df
text_content = tk.Text(root, wrap="word")
text_content.pack(fill="both", expand=True)

# Execute the script automatically when the window is created
execute_script()

# Run the GUI application
root.mainloop()
