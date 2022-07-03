from tkinter import *
from funcionesSql import FxSql

def obtenerCargo():
    id=txt_idCargo.get()
    nom=txt_nombreCargo.get()
    
    FxSql.agregarCargo(id,nom)

def obtenerLaborales():
    id=txt_idLaborales.get()
    area=txt_area.get()
    depa=txt_departamento.get()
    FxSql.agregarDatosLaborales(id,area,depa)

vent = Tk()
vent.title("Ingresar Datos laborales")
vent.geometry("750x500")

# Frames
frameCargos = Frame(vent,bg ="sky blue")
frameCargos.pack(expand=True,fill="both")
frameLaborales = Frame(vent,bg ="light salmon")
frameLaborales.pack(expand=True,fill="both")
# Registrar cargo
lbl_cargos = Label(frameCargos,text="Registrar cargo",bg="yellow")
lbl_cargos.place(x=10,y=10,width=210,height=20)
#
lbl_idCargo = Label(frameCargos,text="ID Cargo:",bg="yellow",anchor="w")
lbl_idCargo.place(x=10,y=40,width=120,height=20)
txt_idCargo = Entry(frameCargos,bg="pink")
txt_idCargo.place(x=140,y=40,width=120,height=20)
#
lbl_nombreCargo = Label(frameCargos,text="Nombre Cargo:",bg="yellow",anchor="w")
lbl_nombreCargo.place(x=10,y=70,width=120,height=20)
txt_nombreCargo = Entry(frameCargos,bg="pink")
txt_nombreCargo.place(x=140,y=70,width=120,height=20)
#
btn_registarCargo = Button(vent,text="Registrar", command=obtenerCargo)
btn_registarCargo.place(x=140,y=100,width=120,height=20)

# Registar Datos laborales
lbl_laborales = Label(frameLaborales,text="Registrar datos laborales",bg="yellow")
lbl_laborales.place(x=10,y=10,width=210,height=20)
#
lbl_idLaborales = Label(frameLaborales,text="ID Labrales:",bg="yellow",anchor="w")
lbl_idLaborales.place(x=10,y=40,width=120,height=20)
txt_idLaborales = Entry(frameLaborales,bg="pink")
txt_idLaborales.place(x=140,y=40,width=120,height=20)
#
lbl_area = Label(frameLaborales,text="Nombre Cargo:",bg="yellow",anchor="w")
lbl_area.place(x=10,y=70,width=120,height=20)
txt_area = Entry(frameLaborales,bg="pink")
txt_area.place(x=140,y=70,width=120,height=20)
#
lbl_departamento = Label(frameLaborales,text="Nombre Departamento:",bg="yellow",anchor="w")
lbl_departamento.place(x=10,y=100,width=120,height=20)
txt_departamento = Entry(frameLaborales,bg="pink")
txt_departamento.place(x=140,y=100,width=120,height=20)
#
btn_registarCargo = Button(frameLaborales,text="Registrar", command=obtenerLaborales)
btn_registarCargo.place(x=140,y=130,width=120,height=20)

vent.mainloop()
