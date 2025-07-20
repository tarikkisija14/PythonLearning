from tkinter import messagebox, ttk

import pandas as pd
import tkinter as tk
import os

from shap import text_plot

csvPath=r"C:\Users\tarik\Desktop\pocetnicki koraci\Sales_Data.csv"

program=tk.Tk()
program.geometry("700x500")
program.title("Sales")


notebook = ttk.Notebook(program)
notebook.pack(fill='both',expand=True)

tab_loading=tk.Frame(notebook)
tab_filter=tk.Frame(notebook)
tab_analysis=tk.Frame(notebook)

notebook.add(tab_loading, text='Ucitavanje CSV')
notebook.add(tab_filter, text='Filter i Analiza')
notebook.add(tab_analysis, text='Jos vise Analize')

#Load tab

textOutput = tk.Text(tab_loading, wrap="none", width=80, height=20)
textOutput.pack(pady=10)



def LoadData():
    try:
        df=pd.read_csv(csvPath)
        print(df.head())
        messagebox.showinfo("Ucitano",f"Ucitano :{len(df)}")
        textOutput.delete('1.0',tk.END)
        tekst=df.head(10).to_string(index=False)
        textOutput.insert(tk.END, tekst)


    except Exception as e:
        messagebox.showerror("Error",f"{e}")

tk.Button(tab_loading,text="Ucitaj Podatke",command=LoadData).pack(pady=40)

#Filter tab

text_analysis = tk.Text(tab_filter, wrap="none", width=80, height=20)
text_analysis.pack(pady=10)


def ShowStats():
    try:
      df=pd.read_csv(csvPath)
      opis=df.describe().to_string()
      text_analysis.delete('1.0',tk.END)
      text_analysis.insert(tk.END,opis)
    except Exception as e:
        messagebox.showerror("Error",f"{e}")


def FilterSales():
    try:
      df=pd.read_csv(csvPath)
      df.columns=df.columns.str.strip()
      filtered = df[df['QuantityOrdered'] > 2]
      text_analysis.delete('1.0',tk.END)
      if filtered.empty:
        text_analysis.insert(tk.END,'Nema podataka')
      else:
        text_analysis.insert(tk.END,filtered.to_string(index=False))
    except Exception as e:
        messagebox.showerror("Error",f"{e}")



tk.Button(tab_filter, text="Prikaži statistiku", font=("Arial", 12), command=ShowStats).pack(pady=5)
tk.Button(tab_filter, text="Filtriraj ", font=("Arial", 12), command=FilterSales).pack(pady=5)



#tab analysis


text_analysis2 = tk.Text(tab_analysis, wrap="none", width=80, height=20)
text_analysis2.pack(pady=10)



def Top10Products():
    try:
      df=pd.read_csv(csvPath)
      group=df.groupby('Product')['QuantityOrdered'].sum().sort_values(ascending=False)
      top10=group.index[:10]
      text_analysis2.delete('1.0',tk.END)
      for p in top10:
          text_analysis2.insert(tk.END,f"{p} \n")
    except Exception as e:
        messagebox.showerror("Error",f"{e}")


tk.Button(tab_analysis, text="Top 10 proizvoda", font=("Arial", 12), command=Top10Products).pack(pady=5)



program.mainloop()
