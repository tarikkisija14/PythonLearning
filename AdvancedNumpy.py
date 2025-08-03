import tkinter as tk
from tkinter import ttk, messagebox
import random
import numpy as np

program=tk.Tk()
program.geometry("600x500")
program.title("Numpy")

notebook = ttk.Notebook(program)
notebook.pack(fill='both',expand=True)

tab_broadcast=tk.Frame(notebook)
notebook.add(tab_broadcast, text='Sabiranje matrica')

tab_slicing=tk.Frame(notebook)
notebook.add(tab_slicing, text='Izmjeni vektor')


tab_vect=tk.Frame(notebook)
notebook.add(tab_vect, text='Vektorizacija')

tab_linal=tk.Frame(notebook)
notebook.add(tab_linal, text='Linearna algebra')

TextOutput = tk.Text(tab_broadcast, width=60, height=20)
TextOutput.pack(pady=10)

def BroadcastMatx():
    matrix1 = np.random.randint(1, 10, (3, 1))
    matrix2 = np.random.randint(1, 10, (1, 4))

    matrix3=matrix1+matrix2

    TextOutput.delete(1.0, tk.END)

    TextOutput.insert(tk.END, "Matrica 1: \n")
    TextOutput.insert(tk.END, f"{matrix1}\n\n")
    TextOutput.insert(tk.END, "Matrica 2: \n")
    TextOutput.insert(tk.END, f"{matrix2}\n\n")
    TextOutput.insert(tk.END, "Matrica 3(sabiranje A i B): \n")
    TextOutput.insert(tk.END, f"{matrix3}")


tk.Button(tab_broadcast,text="Saberi",command=BroadcastMatx).pack(pady=40)

TextOutput1 = tk.Text(tab_slicing, width=60, height=20)
TextOutput1.pack(pady=10)

def Slicing():
    vector=np.arange(1,21)
    original=vector.copy()
    newV=vector[vector>10]

    vector[1::2]=-1
    TextOutput1.delete(1.0, tk.END)

    TextOutput1.insert(tk.END, f"Originalni vektor:\n  {original}\n\n")
    TextOutput1.insert(tk.END, f"Vektor sa elementima vecim od 10 :\n  {newV}\n\n")
    TextOutput1.insert(tk.END,f"Vektor nakon promjene neparnih indeksa: \b {vector}")



tk.Button(tab_slicing,text="Kreiraj Vektor i izmjeni",command=Slicing).pack(pady=40)


TextOutput2 = tk.Text(tab_vect, width=60, height=20)
TextOutput2.pack(pady=10)

def VectorizeFunction():
    def f(x):
        return x**2+2*x+1

    arr=np.arange(-5,6)

    f_vect=np.vectorize(f)

    rez=f_vect(arr)

    TextOutput2.delete(1.0, tk.END)
    TextOutput2.insert(tk.END, f"Ulazni niz: \n {arr}\n\n")
    TextOutput2.insert(tk.END, f"Izlaz x^2+2x+1: {rez}\n\n")



tk.Button(tab_vect,text="Vektorizacija",command=VectorizeFunction).pack(pady=40)

TextOutput3 = tk.Text(tab_linal, width=60, height=20)
TextOutput3.pack(pady=10)

def LinAlgOps():
    m1=np.random.rand(3,3)
    m2=np.random.rand(3,3)

    m3=np.dot(m1,m2)

    detA=np.linalg.det(m1)

    try:
        invA=np.linalg.inv(m1)
    except np.linalg.LinAlgError:
        invA="Matrica m1 nije invertibilna(det=0)"

    TextOutput3.delete(1.0, tk.END)
    TextOutput3.insert(tk.END, f"matrica A:\n{m1}\n\n")
    TextOutput3.insert(tk.END, f"matrica B:\n{m2}\n\n")
    TextOutput3.insert(tk.END, f"A*B:\n{m3}\n\n")
    TextOutput3.insert(tk.END, f"Determinanta matrice A:\n{detA}\n\n")

    if isinstance(invA, str):
        TextOutput3.insert(tk.END, f"Inverzna matrica A:\n{invA}\n")
    else:
        TextOutput3.insert(tk.END, f"Inverzna matrica A:\n{invA}\n")





tk.Button(tab_linal,text="Operacije Linearne Algebre",command=LinAlgOps).pack(pady=40)


program.mainloop()