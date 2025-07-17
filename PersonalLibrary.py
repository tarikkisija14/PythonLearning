import tkinter as tk
import json
import os
from tkinter import messagebox

from joblib.externals.cloudpickle import list_registry_pickle_by_value

from BooksRepository import PrikaziKnjige


class Book:
    def __init__(self,id,naslov,autor,godina):
        self.id=id
        self.naslov=naslov
        self.autor=autor
        self.godina=godina


    def to_dict(self):
        return {
            "id":self.id,
            "naslov":self.naslov,
            "autor":self.autor,
            "godina":self.godina
        }

    @classmethod
    def from_dict(cls,data):
        return cls(data["id"],data["naslov"],data["autor"],data["godina"])


class Library:
    def __init__(self):
        self.books=[]


    def AddBook(self,book):
        self.books.append(book)


    def removeBook(self,book):
        self.books.remove(book)

    def getallbooks(self):
        return self.books


    def saveToJson(self):
        with open("library.json","w") as file:
            json.dump([i.to_dict() for i in self.books],file,indent=4)


    def loadFromJson(self):
        if os.path.exists("library.json"):
            with open("library.json","r") as file:
                try:
                    books = json.load(file)
                    self.books = [Book.from_dict(d) for d in books]
                except json.JSONDecodeError:
                    self.books = []
        else:
            self.books = []




library=Library()
library.loadFromJson()

uinterface1=tk.Tk()
uinterface1.geometry("500x550")
uinterface1.title("Personal Library")

tk.Label(uinterface1, text="Naslov knjige:", font=("Arial", 12)).pack(pady=5)
entry_naslov = tk.Entry(uinterface1, font=("Arial", 12))
entry_naslov.pack(pady=5)

tk.Label(uinterface1, text="Autor:", font=("Arial", 12)).pack(pady=5)
entry_autor = tk.Entry(uinterface1, font=("Arial", 12))
entry_autor.pack(pady=5)

tk.Label(uinterface1, text="Godina:", font=("Arial", 12)).pack(pady=5)
entry_godina = tk.Entry(uinterface1, font=("Arial", 12))
entry_godina.pack(pady=5)


def AddBook():
    naslov=entry_naslov.get().strip()
    autor=entry_autor.get().strip()
    godina=entry_godina.get().strip()

    if not naslov or not autor or not godina:
        messagebox.showerror("Error", "Naslov knjige ne autor")
        return

    new_id=1
    if library.books:
       new_id=max(i.id for i in library.books)+1

    new_book=Book(new_id,naslov,autor,godina)
    library.AddBook(new_book)
    library.saveToJson()

    entry_naslov.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_godina.delete(0, tk.END)

    ShowBooks()





tk.Button(uinterface1, text="Dodaj knjigu", font=("Arial", 14), command=AddBook).pack(pady=10)

listbox = tk.Listbox(uinterface1, font=("Arial", 12), width=40, height=10)
listbox.pack(pady=(10, 5))

def ShowBooks():
    listbox.delete(0, tk.END)
    for i in library.getallbooks():
        listbox.insert(tk.END, f"{i.naslov}-{i.autor}-{i.godina}")

ShowBooks()



def DeleteBook():
    izabrani=listbox.curselection()

    if izabrani:
        indeks=izabrani[0]
        obj=library.books[indeks]
        library.removeBook(obj)
        library.saveToJson()
        ShowBooks()
    else:
        messagebox.showerror("Error", "Odaberite knjigu za brisanje")


tk.Button(uinterface1,text="Obrisi knjigu", font=("Arial", 14), command=DeleteBook).pack(pady=10)

uinterface1.mainloop()