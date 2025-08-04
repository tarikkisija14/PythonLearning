import tkinter as tk

prozor = tk.Tk()
prozor.title("BMI Calculator")
prozor.geometry("400x400")

tk.Label(prozor, text="Weight(kg):",font=("Arial",12)).pack(pady=5)
entry_tezina = tk.Entry(prozor,font=("Arial",12))
entry_tezina.pack()

tk.Label(prozor,text="Height(kg):",font=("Arial",12)).pack(pady=5)
entry_visina = tk.Entry(prozor,font=("Arial",12))
entry_visina.pack()



def izracunaj_bmi():
    try:
        tezina = float(entry_tezina.get())
        visina = float(entry_visina.get())
        visina_m=visina/100

        bmi=tezina/(visina_m ** 2)
        bmi=round(bmi,2)

        if bmi < 18.5:
            status='Neuhranjenost'
        elif 18.5 <= bmi < 25:
            status='Normalna Tezina'
        elif 25 <= bmi < 30:
            status='Prekomjerna tezina'
        else:
            status='Gojaznost'

        rezultat_label.config(text=status,font=("Arial",14),fg="green")
    except:
      rezultat_label.config(text="Nevzacei unos!!",font=("Arial",14),fg="red")

tk.Button(prozor,text="Calculate",font=("Arial",14),command=izracunaj_bmi).pack(pady=10)

rezultat_label=tk.Label(prozor,text="",font=("Arial",14))
rezultat_label.pack(pady=16)


prozor.mainloop()
