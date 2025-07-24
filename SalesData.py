import tkinter as tk
from tkinter import ttk, messagebox

import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from pandas.core import frame

Sales=r"C:\Users\tarik\Desktop\pocetnicki koraci\Sales_Data.csv"
Customers=r"C:\Users\tarik\Desktop\pocetnicki koraci\Customers.csv"

program=tk.Tk()
program.geometry("900x500")
program.title("SalesData")

notebook = ttk.Notebook(program)
notebook.pack(fill='both',expand=True)

tab_loading=tk.Frame(notebook)
tab_cleaning=tk.Frame(notebook)
tab_analysis=tk.Frame(notebook)
tab_Merge=tk.Frame(notebook)

notebook.add(tab_loading, text='Ucitavanje CSV')
notebook.add(tab_cleaning, text='Ciscenje podataka')
notebook.add(tab_analysis, text='Analiza')
notebook.add(tab_Merge, text='Spoji')

# Load tab

textOutput = tk.Text(tab_loading, wrap="none", width=100, height=20)
textOutput.pack(pady=10)

def LoadData():
    try:
      df_sales=pd.read_csv(Sales)
      messagebox.showinfo("Ucitano", f"Ucitano :{len(df_sales)}")
      textOutput.delete('1.0',tk.END)
      textOutput.insert('1.0',df_sales)
    except Exception as e:
        messagebox.showerror("Ucitano",f"{e}")



tk.Button(tab_loading,text="Ucitaj Podatke",command=LoadData).pack(pady=40)


#Clean tab

textClean = tk.Text(tab_cleaning, wrap="none", width=100, height=20)
textClean.pack(pady=10)

def CleanData():
    try:
        df=pd.read_csv(Sales)
        df=df.dropna()

        df['City']=df['PurchaseAddress'].apply(lambda x:x.split(',')[1].strip() if ',' in x else x)

        df['OrderDate']=pd.to_datetime(df['OrderDate'],errors='coerce')
        df['Month']=df['OrderDate'].dt.month
        df['Year']=df['OrderDate'].dt.year

        textClean.delete('1.0',tk.END)
        textClean.insert(tk.END,df.head(10).to_string(index=False))

    except Exception as e:
        messagebox.showerror("Greska",f"{e}")



tk.Button(tab_cleaning,text="Ocisti Podatke",command=CleanData).pack(pady=40)


#Analiza

frame_chart=tk.Frame(tab_analysis)
frame_chart.pack(fill='both',expand=True)

textA = tk.Text(tab_analysis, wrap="none", width=100, height=20)
textA.pack(pady=10)

def ShowStats():
    df=pd.read_csv(Sales)

    df['OrderDate']=pd.to_datetime(df['OrderDate'],errors='coerce')

    df['Month']=df['OrderDate'].dt.month

    monthly=df.groupby('Month')['QuantityOrdered'].sum()

    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    monthly.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_title("Prodaja po mjesecima")
    ax.set_xlabel("Mjesec")
    ax.set_ylabel("Ukupna prodaja")

    for widget in frame_chart.winfo_children():
        widget.destroy()


    canvas=FigureCanvasTkAgg(fig,master=frame_chart)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both',expand=True)


tk.Button(tab_analysis,text="Prikazi",command=ShowStats).pack(pady=40)


#tab Merge

textMerge = tk.Text(tab_Merge, wrap="none", width=100, height=20)
textMerge.pack(pady=10)

def Merge():
    try:
      df_sales=pd.read_csv(Sales)
      df_customers=pd.read_csv(Customers)

      merged_df=pd.merge(df_sales,df_customers,how='inner',on='CustomerID')

      textMerge.delete('1.0',tk.END)
      textMerge.insert(tk.END,merged_df.head(10).to_string(index=False))
    except Exception as e:
        messagebox.showerror("Greska",f"{e}")




tk.Button(tab_Merge,text="Spoji",command=Merge).pack(pady=40)


program.mainloop()
