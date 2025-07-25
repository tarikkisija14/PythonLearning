import tkinter as tk
from tkinter import ttk, messagebox
import random
import numpy as np

program=tk.Tk()
program.geometry("900x500")
program.title("Numpy")

notebook = ttk.Notebook(program)
notebook.pack(fill='both',expand=True)

tab_begginings=tk.Frame(notebook)
notebook.add(tab_begginings, text='Mnozenje matrica')

tab_arrayops=tk.Frame(notebook)
notebook.add(tab_arrayops, text='Operacije nad nizovima')

tab_norm=tk.Frame(notebook)
notebook.add(tab_norm, text='Broadcasting i normalizacija')

tab_gen=tk.Frame(notebook)
notebook.add(tab_gen, text='Generisanje linearnog tipa podataka')

TextOutput = tk.Text(tab_begginings, width=60, height=20)
TextOutput.pack(pady=10)

def MultiplyMatrix():
  matrix1=np.random.randint(1,10,(3,3))
  matrix2=np.random.randint(1,10,(3,3))

  matrix3=np.dot(matrix1,matrix2)

  TextOutput.delete(1.0, tk.END)
  TextOutput.insert(tk.END, "Matrica 1: \n")
  TextOutput.insert(tk.END, f"{matrix1}\n\n")
  TextOutput.insert(tk.END, "Matrica 2: \n")
  TextOutput.insert(tk.END, f"{matrix2}\n\n")
  TextOutput.insert(tk.END, "Matrica 3(mnozenje A i B): \n")
  TextOutput.insert(tk.END, f"{matrix3}")


tk.Button(tab_begginings,text="Pomnozi",command=MultiplyMatrix).pack(pady=40)



program.mainloop()

