import tkinter as tk
import json
import os


userfile="korisnici.json"

uinterface=tk.Tk()
uinterface.title("Login")
uinterface.geometry("400x400")

loginform=tk.Frame(uinterface)

tk.Label(loginform,text="Username",font=("Arial",14)).pack(pady=5)
entry_username=tk.Entry(loginform,font=("Arial",14))
entry_username.pack()

tk.Label(loginform,text="Password",font=("Arial",14)).pack(pady=5)
entry_password=tk.Entry(loginform,font=("Arial",14),show="*")
entry_password.pack()

regform=tk.Frame(uinterface)

tk.Label(regform,text="New Username:",font=("Arial",14)).pack(pady=5)
entry_new_user=tk.Entry(regform)
entry_new_user.pack()

tk.Label(regform,text="New Password:",font=("Arial",14)).pack(pady=5)
entry_new_password=tk.Entry(regform,show="*")
entry_new_password.pack()




def loadUsers():
    if os.path.exists(userfile):
        with open(userfile,"r") as f:
            return json.load(f)
    return{}

def saveUsers(users):
    with open(userfile,"w") as f:
        json.dump(users,f)

def Registration():
    username = entry_new_user.get()
    password = entry_new_password.get()

    if len(password) < 6:
        label_status_reg.config(text="Password cant have less than 6 characters")
        return

    users=loadUsers()

    if username in users:
        label_status_reg.config(text="Username already registered",fg="orange")
        return
    else:
        users[username]=password
        saveUsers(users)
        label_status_reg.config(text="Username registered",fg="green")



def Login():
    username=entry_username.get()
    password=entry_password.get()

    users=loadUsers()

    if username in users and users[username]==password:
       label_status.config(text="Login successful",fg="green")
    else:
        label_status.config(text="Login failed",fg="red")



def ShowReg():
    loginform.pack_forget()
    regform.pack(pady=10)

def ShowLogin():
    regform.pack_forget()
    loginform.pack(pady=10)



tk.Button(loginform,text="Log in",command=Registration).pack(pady=10)
tk.Button(uinterface,text="Register here",command=ShowReg).pack(pady=50)

label_status=tk.Label(loginform,text="",font=("Arial",10))
label_status.pack(pady=10)
loginform.pack()


tk.Button(regform,text="Register",command=Registration).pack(pady=10)
tk.Button(regform,text="Back to Login",command=ShowLogin).pack()


label_status_reg=tk.Label(regform,text="",font=("Arial",10))
label_status_reg.pack(pady=10)


uinterface.mainloop()