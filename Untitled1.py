
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import messagebox
import calendar
import time

def signin_page():
    signup = Tk()
    signup.mainloop()
    
    
window= Tk()
window.title("NoMoney Bank")
window.geometry("600x600")
label = Label(text="NoMoney Bank")
label.place(x=80,y=50)
label.config(font=("Courier", 44))
cotton_type=StringVar(window)
button_signup =  Button(text="SignUP")
button_signup.place(x=200,y=150)
button_signup.config(font=("Courier", 20))

button_signin =  Button(text="Sign In")
button_signin.place(x=200,y=250)
button_signin.config(font=("Courier", 20))

button_admin =  Button(text="Admin Sign In")
button_admin.place(x=200,y=350)
button_admin.config(font=("Courier", 20))

button_exit =  Button(text="Exit")
button_exit.place(x=200,y=450)
button_exit.config(font=("Courier", 20))


window.mainloop()

