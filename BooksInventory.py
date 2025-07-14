import sqlite3
import tkinter as tk
from tkinter import messagebox

from pyexpat.errors import messages

db = sqlite3.connect('books.db')
cursor=db.cursor()




uinterface=tk.Tk()
uinterface.geometry('500x600')
uinterface.title('Books Inventory')

tk.Label(uinterface,text="Naslov knjige",font=("Arial",14)).pack(pady=5)
entry_naslov=tk.Entry(uinterface,font=("Arial",12))
entry_naslov.pack()

tk.Label(uinterface,text="Autor",font=("Arial",14)).pack(pady=5)
entry_autor=tk.Entry(uinterface,font=("Arial",12))
entry_autor.pack()

tk.Label(uinterface,text="Godina:",font=("Arial",14)).pack(pady=5)
entry_godina=tk.Entry(uinterface,font=("Arial",12))
entry_godina.pack()


def DodajKnjigu():
    naziv=entry_naslov.get()
    autor=entry_autor.get()
    godina=entry_godina.get()

    if not naziv or not autor or not godina:
        messagebox.showerror("Greška", "Popunite sva polja")
        return

    cursor.execute("INSERT INTO books(title,author,year) VALUES(?,?,?)",(naziv,autor,godina))
    db.commit()

    entry_naslov.delete(0,tk.END)
    entry_autor.delete(0,tk.END)
    entry_godina.delete(0,tk.END)

    PrikaziKnjige()


tk.Button(uinterface, text="Dodaj knjigu", font=("Arial", 14), command=DodajKnjigu).pack(pady=10)

def PrikaziKnjige():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT id,title,author,year FROM books")
    for id,title,author,year in cursor.fetchall():
        listbox.insert(tk.END, f"{id}-{title}-{author}-{year}")

tk.Button(uinterface, text="Prikazi Knjige", font=("Arial", 14), command=PrikaziKnjige).pack(pady=30)

listbox = tk.Listbox(uinterface, font=("Arial", 12), width=40, height=10)
listbox.pack(pady=(10, 5))



def ObrisiKnjigu():
    izabrani=listbox.curselection()

    if izabrani:
        tekst = listbox.get(izabrani[0])
        id = int(tekst.split("-")[0].strip())
        cursor.execute("DELETE FROM books WHERE id=?",(id,))
        db.commit()
        PrikaziKnjige()
    else:
        messagebox.showerror("Greška", "Odaberite Knjigu")


tk.Button(uinterface, text="Obrisi knjigu", font=("Arial", 14), command=ObrisiKnjigu).pack(padx=10)


uinterface.mainloop()
