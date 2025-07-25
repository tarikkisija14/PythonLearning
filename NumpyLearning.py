import tkinter as tk
from tkinter import ttk, messagebox
import random
import numpy as np

program=tk.Tk()
program.geometry("600x500")
program.title("Numpy")

notebook = ttk.Notebook(program)
notebook.pack(fill='both',expand=True)

tab_multiply=tk.Frame(notebook)
notebook.add(tab_multiply, text='Mnozenje matrica')

tab_arrayops=tk.Frame(notebook)
notebook.add(tab_arrayops, text='Analiza vektora')

tab_norm=tk.Frame(notebook)
notebook.add(tab_norm, text='Broadcasting i normalizacija')

tab_gen=tk.Frame(notebook)
notebook.add(tab_gen, text='Generisanje linearnog tipa podataka')

TextOutput = tk.Text(tab_multiply, width=60, height=20)
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


tk.Button(tab_multiply,text="Pomnozi",command=MultiplyMatrix).pack(pady=40)


#tab2

TextOutput2 = tk.Text(tab_arrayops, width=60, height=20)
TextOutput2.pack(pady=10)

def AnalyzeVector():
  v=np.random.randint(1,100,(10,))

  sum=np.sum(v)
  mean=np.mean(v)
  std=np.std(v)

  #reshape vektora u matricu 2x5
  reshaped=v.reshape((2,5))

  TextOutput2.delete(1.0, tk.END)

  TextOutput2.insert(tk.END, f"Orginalni vektor: \n")
  TextOutput2.insert(tk.END, f"{v} \n\n")
  TextOutput2.insert(tk.END, f"Suma:{sum} \n")
  TextOutput2.insert(tk.END, f"Sredina:{mean} \n")
  TextOutput2.insert(tk.END, f"Std:{std} \n\n")
  TextOutput2.insert(tk.END, f"Reshaped vektor u matricu :\n")
  TextOutput2.insert(tk.END, f"{reshaped}")



tk.Button(tab_arrayops,text="Analiziraj",command=AnalyzeVector).pack(pady=40)

#tab3

TextOutput3 = tk.Text(tab_norm, width=60, height=20)
TextOutput3.pack(pady=10)


def Normalize():
  matrix = np.random.randint(0, 100, size=(100, 3))
  min_col=matrix.min(axis=0)
  max_col=matrix.max(axis=0)

  norm=(matrix-min_col)/(max_col-min_col)

  TextOutput3.delete(1.0, tk.END)

  TextOutput3.insert(tk.END, "Prije normalizacije: \n")
  TextOutput3.insert(tk.END, f"{matrix}\n\n")

  TextOutput3.insert(tk.END, "Poslije normalizacije: \n")
  TextOutput3.insert(tk.END, f"{norm}")



tk.Button(tab_norm,text="Normalizuj",command=Normalize).pack(pady=40)


#tab4

TextOutput4 = tk.Text(tab_gen, width=60, height=20)
TextOutput4.pack(pady=10)

def GenerateLinearData():
  X=np.random.rand(100)

  noise=np.random.randn(100)*0.1

  y=3*X+5+noise

  TextOutput4.delete(1.0, tk.END)

  TextOutput4.insert(tk.END, f"Prvih 10 vrijednosti x i y:\n\n")
  for i in range(10):
    TextOutput4.insert(tk.END,
                       f"X[{i}]: {X[i]:.4f}   y[{i}]: {y[i]:.4f}\n")




tk.Button(tab_gen,text="Generisi linearne podatke",command=GenerateLinearData).pack(pady=40)


program.mainloop()

