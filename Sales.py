from tkinter import messagebox

import pandas as pd
import tkinter as tk
import os

from shap import text_plot

csvPath=r"C:\Users\tarik\Desktop\pocetnicki koraci\Sales_Data.csv"

program=tk.Tk()
program.geometry("600x500")
program.title("Sales")

textOutput = tk.Text(program, wrap="none", width=80, height=20)
textOutput.pack(pady=10)



def LoadData():
    try:
        df=pd.read_csv(csvPath)
        print(df.head())
        messagebox.showinfo("Ucitano",f"{len(df)}")
        textOutput.delete('1.0',tk.END)
        tekst=df.head(10).to_string(index=False)
        textOutput.insert(tk.END, tekst)


    except Exception as e:
        messagebox.showerror("Error",f"{e}")

tk.Button(program,text="Ucitaj Podatke",command=LoadData).pack(pady=40)




program.mainloop()
