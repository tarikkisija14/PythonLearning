import tkinter as tk
import datetime as dt
import json
import os
from tkinter import messagebox

tasks=[]
userfile="tasks.json"

window=tk.Tk()
window.title("Task Scheduler")
window.geometry("500x600")


tk.Label(window,text="Naziv zadatka",font=("Arial",14)).pack(pady=5)
entry_naziv=tk.Entry(window,font=("Arial",12))
entry_naziv.pack()

tk.Label(window,text="Opis zadatka",font=("Arial",14)).pack(pady=5)
entry_opis=tk.Entry(window,font=("Arial",12))
entry_opis.pack()

tk.Label(window,text="Datum",font=("Arial",14)).pack(pady=5)
entry_datum=tk.Entry(window,font=("Arial",12))
entry_datum.pack()

tk.Label(window,text="Vrijeme",font=("Arial",14)).pack(pady=5)
entry_vrijeme=tk.Entry(window,font=("Arial",12))
entry_vrijeme.pack()

listbox=tk.Listbox(window,font=("Arial",14))
listbox.pack(pady=10)
listbox.config(width=30, height=10)
listbox.config(bg="white", fg="black", font=('Arial', 12))



def LoadTasks():
    global tasks
    if os.path.exists(userfile):
       with open(userfile) as f:
        tasks = json.load(f)
        for i in tasks:
               listbox.insert(tk.END,i)
    else:
        return tasks


def SaveTasks():
    with open(userfile, 'w') as f:
        json.dump(tasks, f)




def AddTask():
    naziv=entry_naziv.get()
    opis=entry_opis.get()
    datum=entry_datum.get()
    vrijeme=entry_vrijeme.get()
    if not naziv:
        messagebox.showerror("Naziv","Naziv zadatka")
        return

    try:
         datumvrijeme=f"{datum} {vrijeme}"
         datumvrijeme = dt.datetime.strptime(f"{datum} {vrijeme}", "%Y-%m-%d %H:%M")
    except ValueError:
        messagebox.showerror("Greska","Neispravan format")
        return

    if datumvrijeme<=dt.datetime.now():
        messagebox.showerror("Greska","Datum i vrijeme moraju biti u buducnosti")
        return


    zadatak={
        'naziv':naziv,
        'opis':opis,
        'datumvrijeme': datumvrijeme.strftime("%Y-%m-%d %H:%M"),
         'kreirano':  dt.datetime.now().strftime("%Y-%m-%d %H:%M")

    }

    tasks.append(zadatak)

    listbox.insert(tk.END,f"{naziv} {datumvrijeme.strftime('%Y-%m-%d')}")

    entry_naziv.delete(0, tk.END)
    entry_opis.delete(0, tk.END)
    entry_datum.delete(0, tk.END)
    entry_vrijeme.delete(0, tk.END)

    SaveTasks()


def DeleteTask():
    izabrani=listbox.curselection()

    if izabrani:
        listbox.delete(izabrani[0])
        SaveTasks()
    else:
        messagebox.showerror("Greska","Niste izabrali nista")






tk.Button(window,text="Dodaj zadatak",font=("Arial",14),command=AddTask).pack(pady=10)
tk.Button(window,text="Obrisi zadatak",font=("Arial",14),command=DeleteTask).pack(pady=10)

LoadTasks()
window.mainloop()