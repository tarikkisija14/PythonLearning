import os
import tkinter as tk

from numpy.matlib import empty

import json

window=tk.Tk()
window.geometry("400x500")
window.title("ToDoList")

userfile="zadaci.json"


tk.Label(window,text="Unesi zadatak",font=("Arial",14)).pack(pady=20)
entry_todo=tk.Entry(window,font=("Arial",12))
entry_todo.pack()

def DodajZadatak():
    tekst=entry_todo.get().strip()
    if tekst=="":
        tk.Label(window,text="Greska, niste unijeli nista",font=("Arial",14)).pack(pady=10)
    else:
        listbox.insert(tk.END, tekst)
        entry_todo.delete(0, tk.END)
    SaveFile()



tk.Button(window,text="Dodaj zadatak",font=("Arial",14),command=DodajZadatak).pack(pady=10)



listbox=tk.Listbox(window,font=("Arial",14))
listbox.pack(pady=10)



listbox.config(width=30, height=10)
listbox.config(bg="white", fg="black", font=('Arial', 12))

def ObrisiZadatak():
    izabrani=listbox.curselection()

    if izabrani:
        listbox.delete(izabrani[0])
    else:
        tk.Label(window,text="Greska,nista nije selektovano",fg="red",font=("Arial",14)).pack(pady=10)
    SaveFile()




def LoadFile():
    if os.path.exists(userfile):
        with open(userfile,"r") as f:
            try:
                lista=json.load(f)
                for i in lista:
                    listbox.insert(tk.END, i)
            except json.decoder.JSONDecodeError:
                print("Greska u citanju JSON fajla")


def SaveFile():
    lista=listbox.get(0,tk.END)
    with open(userfile,"w") as file:
        json.dump(list(lista),file,indent=4)




tk.Button(window, text="Spasi zadatke", font=("Arial", 14), command=SaveFile).pack(pady=10)
tk.Button(window,text="Obrisi zadatak",font=("Arial",14),command=ObrisiZadatak).pack(pady=10)


LoadFile()
window.mainloop()

