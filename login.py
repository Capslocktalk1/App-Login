import tkinter as tk
from tkinter import messagebox

creadentials = {"admin":"admin123" , "user1" : "password1"}

def validateLogin():
    username = inputUser.get()
    password = inputPassword.get()
    
    if username in creadentials and creadentials[username] == password:
        messagebox.showinfo("Login Status" , "Login Successfull")
    else:
        messagebox.showerror("Login status" , "invalid username and password")
        
def clear():
    inputUser.delete(0, tk.END)
    inputPassword.delete(0, tk.END)    

root = tk.Tk()
root.title("Login Application")
root.geometry('600x400')

userLabel = tk.Label(root, text="Username: ")
userLabel.pack(pady=5)
inputUser = tk.Entry(root)
inputUser.pack(pady=5)

passwordLabel = tk.Label(root, text="password")
passwordLabel.pack(pady=5)
inputPassword = tk.Entry(root)
inputPassword.pack(pady=5)


btnLogin = tk.Button(root, text="Login", command=clear , bg = "blue" , fg = "white" , font = ('Arial' , 15))
btnLogin.pack(pady=5)

btnClear = tk.Button(root, text="Clear", command=clear , bg = "red" , fg = "white" , font = ('Arial' , 15))
btnClear.pack(pady=5)

root.mainloop()