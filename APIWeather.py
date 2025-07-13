import tkinter as tk
import requests
import json

apikey="44b65f5328eec558bd9391f0748a94b8"


window=tk.Tk()
window.title("APIWeather")
window.geometry("300x300")

tk.Label(window,text="Unesi grad: ",font=("Arial",12)).pack(pady=5)
entry_grad=tk.Entry(window,font=("Arial",12))
entry_grad.pack()

prognoza_label = tk.Label(window, text="", font=("Arial", 14))
prognoza_label.pack(pady=10)


def GetPrognozu():

   grad=entry_grad.get()

   if not grad:
       prognoza_label.config(text="unesite naziv grada",fg="red")
       return

   geourl = url = f"http://api.openweathermap.org/geo/1.0/direct?q={grad}&limit=1&appid={apikey}"

   try:
       geoodg=requests.get(url)
   except:
       prognoza_label.config(text="Greska pri spajanju",fg="red")
       return

   if geoodg.status_code != 200:
       prognoza_label.config(text=f"Greška kod geokodiranja: {geoodg.status_code}", fg="red")
       return

   geopod=geoodg.json()

   if not geopod:
       prognoza_label.config(text="Grad nije pronađen", fg="red")
       return

   lat = geopod[0]['lat']
   lon = geopod[0]['lon']

   vrijemeurl=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}&units=metric&lang=hr"

   try:
       vrijemeodg=requests.get(vrijemeurl)
   except:
       prognoza_label.config(text="Greška pri spajanju na vremensku prognozu", fg="red")
       return

   if vrijemeodg.status_code != 200:
       prognoza_label.config(text=f"Greška kod dohvata vremena: {vrijemeodg.status_code}", fg="red")
       return

   vrijemepod=vrijemeodg.json()

   temp=vrijemepod['main']['temp']
   opis=vrijemepod['weather'][0]['description']
   vjetar=vrijemepod['wind']['speed']

   tekst=(f"Grad:{grad}\n"
          f"Tempreatura: {temp}\n"
          f"Opis:{opis}\n"
          f"Vjetar: {vjetar}\n")
   prognoza_label.config(text=tekst, fg="black")



tk.Button(window,text="Prikazi prognozu",font=("Arial",14),command=GetPrognozu).pack(pady=10)



window.mainloop()

