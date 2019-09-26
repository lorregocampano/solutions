#GUI with two windows, one for login and a second for operate a function
#main window and GUI

window = Tk()
window.resizable(width=FALSE, height=FALSE)
window.title("Proceso de Liquidación")
window.geometry("300x200")

#box and labels for user and password

username_text = Label(window, text="Usuario:")
username_guess = Entry(window)
password_text = Label(window, text="Password:")
password_guess = Entry(window, show="*")

#login button
attempt_login = Button(text="Login", command=try_login)

username_text.pack()
username_guess.pack()
password_text.pack()
password_guess.pack()
attempt_login.pack()
#ventana principal
window.mainloop()

#define an user and a pass
username = ("luis")
password = ("1234")

#function for close the first login window

def close_window(): 
    window.destroy()
    
#Function for login and conditions

def try_login():
    print("Tratando de loguear...")
    if username_guess.get() == username:
        messagebox.showinfo("Información correcta", "Has ingresado", icon="info")
        close_window()
        ventana()
    else:
        messagebox.showinfo("Error en información", "Por favor ingresa credenciales correctas", icon="warning")

#GUI for function, second window

def ventana():

    vtn = Tk()
    vtn.geometry("300x200")
    vtn.title("PUT THE TITLE")

    boton = Button(vtn, text = "button's name",command = PUT HERE THE FUNCTION TO EXECUTE)
    boton.place(x = 50,y = 50)

    boton2 = Button(vtn, text = "second button's name", command = PUT A SECOND FUCTION TO EXECUTE)
    boton2.place(x = 50,y = 90)

    vtn.mainloop()





