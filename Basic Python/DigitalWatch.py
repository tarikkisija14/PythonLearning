import tkinter as tk
import datetime as dt

prozor=tk.Tk()
prozor.title("Digitalni Sat")
prozor.geometry("300x150")
prozor.configure(bg="black")

label=tk.Label(prozor,font=("Courier",40,"bold"),fg="lime",bg="black")
label.pack(expand=True, fill="both")


def azuriraj_vrijeme():
    trenutno=dt.datetime.now().strftime(" %H:%M:%S")
    label.config(text=trenutno)
    prozor.after(1000,azuriraj_vrijeme)

azuriraj_vrijeme()

prozor.mainloop()