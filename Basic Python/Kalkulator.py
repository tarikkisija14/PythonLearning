import tkinter as tk #import tkinter biblioteke


prozor=tk.Tk()#pokretanje glavnog prozora
prozor.title("Kalkulator")
prozor.geometry("400x300")#dimnezije prozora

unos=tk.Entry(prozor,font=("Arial",20,"bold"),borderwidth=5,relief="ridge",justify="right")
unos.pack(padx=10,pady=10,fill="x")

def izracunaj():
    izraz=unos.get()
    try:
        rezultat=eval(izraz)
        unos.delete(0,tk.END)
        unos.insert(0,str(rezultat))
    except ZeroDivisionError:
           unos.delete(0,tk.END)
           unos.insert(0,"Nije dozvoljeno djeljenje s nulom")
    except Exception :
        unos.delete(0, tk.END)
        unos.insert(0, "nevalidan izraz")

def obrisi():
    unos.delete(0,tk.END)


buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]


def dodaj_tekst(t):
    trenutni = unos.get()
    unos.delete(0, tk.END)
    unos.insert(0, trenutni + t)


for red in buttons:
    okvir=tk.Frame(prozor)
    okvir.pack(expand=True,fill="both")
    for dugme in red:
        if dugme== '=':
            komanda=izracunaj
        elif dugme == 'C':
            komanda=obrisi

        else:
            komanda = lambda t=dugme: dodaj_tekst(t)
        b = tk.Button(okvir, text=dugme, font=("Arial", 18), command=komanda)
        b.pack(side="left", expand=True, fill="both")


prozor.mainloop()