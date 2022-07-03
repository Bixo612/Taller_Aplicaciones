from tkinter import *
from funcionesSql import FxSql


vent = Tk()
vent.title("Ingresar Datos laborales")
vent.geometry("750x500")

def obtenerCargo():
    id=txt_idCargo.get()
    nom=txt_nombreCargo.get()
    FxSql.agregarCargo(id,nom)

# Pocisionamiento de elementos
lbl_cargos = Label(vent,text="Registrar cargo",bg="yellow")
lbl_cargos.place(x=10,y=10,width=210,height=20)
#
lbl_idCargo = Label(vent,text="ID Cargo:",bg="yellow",anchor="w")
lbl_idCargo.place(x=10,y=40,width=100,height=20)
txt_idCargo = Entry(vent,bg="pink")
txt_idCargo.place(x=120,y=40,width=100,height=20)
#
lbl_nombreCargo = Label(vent,text="Nombre Cargo:",bg="yellow",anchor="w")
lbl_nombreCargo.place(x=10,y=70,width=100,height=20)
txt_nombreCargo = Entry(vent,bg="pink")
txt_nombreCargo.place(x=120,y=70,width=100,height=20)
#
btn_registarCargo = Button(vent,text="Registrar", command=obtenerCargo)
btn_registarCargo.place(x=120,y=100,width=100,height=20)







vent.mainloop()
