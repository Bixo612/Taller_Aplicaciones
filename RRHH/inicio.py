from tkinter import *

def fx_pass():
    pass

vent = Tk()
vent.title("Inicio")
vent.geometry("230x130")

# defincion de elementos
lbl_bienvenido = Label(vent,text="Bienvenido",bg="yellow")
lbl_idUsuario = Label(vent,text="Id de Usuario",bg="yellow",anchor="w")
lbl_clave = Label(vent,text="Contraseña",bg="yellow",anchor="w") 
txt_idUsuario = Entry(vent,bg="pink")
txt_clave = Entry(vent,bg="pink",show="*")
btn_ingresar = Button(vent,text="Ingresar", command=fx_pass)
# pocision de elementos
lbl_bienvenido.place(x=10,y=10,width=210,height=20)
lbl_idUsuario.place(x=10,y=40,width=100,height=20)
lbl_clave.place(x=10,y=70,width=100,height=20)
txt_idUsuario.place(x=120,y=40,width=100,height=20) 
txt_clave.place(x=120,y=70,width=100,height=20) 
btn_ingresar.place(x=120,y=100,width=100,height=20)

vent.mainloop()