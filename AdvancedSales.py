import tkinter as tk
from tkinter import ttk, messagebox

import pandas as pd

CsvPath=r"C:\Users\tarik\Desktop\pocetnicki koraci\SalesforCleaning.csv"

program=tk.Tk()
program.geometry("700x500")
program.title("Uredjivanje Salesa")

notebook = ttk.Notebook(program)
notebook.pack(fill='both',expand=True)

tab_loading=tk.Frame(notebook)
notebook.add(tab_loading, text='Ucitavanje CSV')


tab_duplicates=tk.Frame(notebook)
notebook.add(tab_duplicates, text='Ciscenje Duplikata ')

tab_nans=tk.Frame(notebook)
notebook.add(tab_nans, text='Ciscenje praznih vrijednosti ')



textOutput = tk.Text(tab_loading, wrap="none", width=80, height=20)
textOutput.pack(pady=10)

def LoadData():
    try:
      df = pd.read_csv(CsvPath, on_bad_lines='skip', engine='python')

      textOutput.delete('1.0',tk.END)
      tekst = df.to_string(index=False)
      textOutput.insert(tk.END, tekst)
    except Exception as e:
        messagebox.showerror("Greska",f"{e}")


tk.Button(tab_loading,text="Ucitaj Podatke",command=LoadData).pack(pady=40)


def EraseDuplicates():
    df = pd.read_csv(CsvPath, on_bad_lines='skip', engine='python')
    print("Broj redova prije ciscenja:", len(df))
    duplicates=df.duplicated()

    print("Broj duplikata: ",duplicates.sum())
    df_clened=df.drop_duplicates()

    print("Broj redova nakon uklanjanja ", len(df_clened))

    df_clened.to_csv(r"C:\Users\tarik\Desktop\pocetnicki koraci\SalesCleaned.csv", index=False)


tk.Button(tab_duplicates,text="Ukloni Duplikate",command=EraseDuplicates).pack(pady=40)


CsvCleaned=r"C:\Users\tarik\Desktop\pocetnicki koraci\SalesCleaned.csv"


def CleanNans():
    df = pd.read_csv(CsvCleaned, on_bad_lines='skip', engine='python')
    nans = df.isnull().sum()
    print("Broj praznih kolona:", len(nans))
    maxid=df['OrderID'].dropna().max()
    for i in range(len(df)):
        if pd.isna(df.loc[i, 'OrderID']):
            maxid += 1
            df.loc[i, 'OrderID'] = maxid

    df['QuantityOrdered']=df['QuantityOrdered'].fillna(df['QuantityOrdered'].mean())

    df.to_csv("SalesCleaned1",index=False)



tk.Button(tab_nans,text="Ocisti Nulte vrijednosti",command=CleanNans).pack(pady=40)





program.mainloop()










