import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

db=sqlite3.connect("SMS.db")
cursor=db.cursor()


uinterface=tk.Tk()
uinterface.geometry('500x600')
uinterface.title('Student Management System')

notebook = ttk.Notebook(uinterface)
notebook.pack(fill='both',expand=True)

tab_students=tk.Frame(notebook)
tab_courses=tk.Frame(notebook)
tab_enrollments=tk.Frame(notebook)

notebook.add(tab_students, text='Studenti')
notebook.add(tab_courses, text='Kursevi')
notebook.add(tab_enrollments, text='Upisi')


#students

tk.Label(tab_students,text="Ime",font=("Arial",14)).pack(pady=5)
entry_ime=tk.Entry(tab_students,font=("Arial",12))
entry_ime.pack()

tk.Label(tab_students,text="Prezime",font=("Arial",14)).pack(pady=5)
entry_prezime=tk.Entry(tab_students,font=("Arial",12))
entry_prezime.pack()

tk.Label(tab_students,text="Godina:",font=("Arial",14)).pack(pady=5)
entry_godina=tk.Entry(tab_students,font=("Arial",12))
entry_godina.pack()

def DodajStudenta():
    ime=entry_ime.get()
    prezime=entry_prezime.get()
    godina=entry_godina.get()

    if not ime or not prezime or not godina:
        messagebox.showerror("Error", "Unesite podatke u sva polja!")
        return

    cursor.execute("Insert into students(ime,prezime,godina) values(?,?,?)",(ime,prezime,godina))
    db.commit()

    entry_ime.delete(0, tk.END)
    entry_prezime.delete(0, tk.END)
    entry_godina.delete(0, tk.END)

    PrikaziStudente()


tk.Button(tab_students, text="Dodaj Studenta", font=("Arial", 14), command=DodajStudenta).pack(pady=10)

def PrikaziStudente():
    listbox.delete(0, tk.END)
    cursor.execute("select * from students")
    for id,ime,prezime,godina in cursor.fetchall():
        listbox.insert(tk.END, f"{id}-{ime}-{prezime}-{godina}")



listbox = tk.Listbox(tab_students, font=("Arial", 12), width=40, height=10)
listbox.pack(pady=(10, 5))
PrikaziStudente()


def ObrisiStudente():
    izabrani=listbox.curselection()

    if izabrani:
        tekst=listbox.get(izabrani[0])
        id = int(tekst.split("-")[0].strip())
        cursor.execute("Delete  FROM students WHERE id=?",(id,))
        PrikaziStudente()
    else:
        messagebox.showerror("Error", "Odaberite studenta!")




tk.Button(tab_students, text="Obrisi Studenta", font=("Arial", 14), command=ObrisiStudente).pack(pady=10)


#Courses

tk.Label(tab_courses,text="Naziv",font=("Arial",14)).pack(pady=5)
entry_naziv=tk.Entry(tab_courses,font=("Arial",12))
entry_naziv.pack()

tk.Label(tab_courses,text="Profesor",font=("Arial",14)).pack(pady=5)
entry_prof=tk.Entry(tab_courses,font=("Arial",12))
entry_prof.pack()


def DodajKurs():
    naziv=entry_naziv.get()
    prof=entry_prof.get()

    if not naziv or not prof:
        messagebox.showerror("Error", "Unesite podatke u sva polja!")
        return

    cursor.execute("insert into courses(naziv,profesor) values(?,?)",(naziv,prof,))
    db.commit()

    entry_naziv.delete(0, tk.END)
    entry_prof.delete(0, tk.END)
    PrikaziKurseve()

tk.Button(tab_courses, text="Dodaj Kurs", font=("Arial", 14), command=DodajKurs).pack(pady=10)


def PrikaziKurseve():
    listbox1.delete(0, tk.END)
    cursor.execute("select * from courses")
    for id,naziv,profesor in cursor.fetchall():
        listbox1.insert(tk.END, f"{id}-{naziv}-{profesor}")


listbox1 = tk.Listbox(tab_courses, font=("Arial", 12), width=40, height=10)
listbox1.pack(pady=(10, 5))
PrikaziKurseve()


def ObrisiKurs():
    izabrani=listbox1.curselection()

    if izabrani:
        tekst = listbox1.get(izabrani[0])
        id = int(tekst.split("-")[0].strip())
        cursor.execute("Delete  FROM courses WHERE id=?", (id,))
        PrikaziKurseve()
    else:
        messagebox.showerror("Error", "Odaberite kurs!")


tk.Button(tab_courses, text="Obrisi Kurs", font=("Arial", 14), command=ObrisiKurs).pack(pady=10)

#enrollments

tk.Label(tab_enrollments,text="StudentId",font=("Arial",14)).pack(pady=5)
entry_studentid=tk.Entry(tab_enrollments,font=("Arial",12))
entry_studentid.pack()

tk.Label(tab_enrollments,text="KursId",font=("Arial",14)).pack(pady=5)
entry_kursid=tk.Entry(tab_enrollments,font=("Arial",12))
entry_kursid.pack()

def DodajUpis():

    studentid=entry_studentid.get()
    kursid=entry_kursid.get()

    if not studentid or not kursid:
        messagebox.showerror("Error", "Unesite podatke u sva polja!")
        return
    try:
        studenti_id = int(studentid)
        kurs_id = int(kursid)

        cursor.execute("SELECT 5 FROM students WHERE id=?", (studenti_id,))
        if not cursor.fetchone():
            messagebox.showerror("Error", "Student sa unijetim ID ne postoji!")
            return

        cursor.execute("SELECT 5 FROM courses WHERE id=?", (kurs_id,))
        if not cursor.fetchone():
            messagebox.showerror("Error", "Kurs sa unijetim ID ne postoji!")
            return



        cursor.execute("insert into enrollments (StudentId,CourseId) values(?,?)",(studenti_id,kurs_id))
        db.commit()

        entry_studentid.delete(0, tk.END)
        entry_kursid.delete(0, tk.END)
        PrikaziUpise()
    except ValueError:
        messagebox.showerror("Error", "ID mora biti broj!")
    except sqlite3.IntegrityError as e:
        if "FOREIGN KEY" in str(e):
            messagebox.showerror("Error", "Nepostojeći student ili kurs!")
        elif "UNIQUE" in str(e):
            messagebox.showerror("Error", "Ovaj student je već upisan na ovaj kurs!")
        else:
            messagebox.showerror("Error", f"Došlo je do greške: {str(e)}")




tk.Button(tab_enrollments, text="Dodaj Upis", font=("Arial", 14), command=DodajUpis).pack(pady=10)

def PrikaziUpise():
    listbox2.delete(0, tk.END)


    cursor.execute("""
          SELECT e.Id, s.ime, s.prezime, c.naziv
          FROM enrollments e
          JOIN students s ON e.StudentId = s.Id
          JOIN courses c ON e.CourseId = c.Id
      """)

    for eid, ime, prezime, naziv_kursa in cursor.fetchall():
        tekst = f"{eid} - {ime} {prezime} - {naziv_kursa}"
        listbox2.insert(tk.END, tekst)




listbox2 = tk.Listbox(tab_enrollments, font=("Arial", 12), width=40, height=10)
listbox2.pack(pady=(10, 5))
PrikaziUpise()



def ObrisiUpis():
    izabrani=listbox2.curselection()

    if izabrani:
      tekst=listbox2.get(izabrani[0])
      id=int(tekst.split("-")[0].strip())

      cursor.execute("DELETE FROM enrollments WHERE id = ?", (id,))
      db.commit()

      PrikaziUpise()
    else:
        messagebox.showerror("Greška", "Odaberite upis koji želite obrisati!")


tk.Button(tab_enrollments, text="Obrisi Upis", font=("Arial", 14), command=ObrisiUpis).pack(pady=10)







notebook.mainloop()