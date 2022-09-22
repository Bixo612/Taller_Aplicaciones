from tkinter import *
from webbrowser import get
from funcionesSql import FxSql

def obtenerTrabajador():
    rut = txt_rut.get()
    nombre1 = txt_primerNombre.get()
    nombre2 = txt_segundoNombre.get()
    apellido1 = txt_primerApellido.get()
    apellido2 = txt_segundoApellido.get()
    fechaNacimiento = txt_fechaNacimiento.get()
    sexo = txt_sexo.get()
    id = txt_id.get()
    tel = txt_telefono.get()
    direccion = txt_direccion.get()
    rol = opt_rol.get()
    FxSql.agregarPersona(rut,nombre1,nombre2,apellido1,apellido2,fechaNacimiento,sexo)
    FxSql.agregarTrabajador(rut,id,"Activo",tel,direccion,rol,)

def generarId():
    pass

vent = Tk()
vent.title("Ingresar Trabajadores")
vent.geometry("660x500")

#AgregarTrbajadores
frameTrabajadores = Frame(vent,bg = "lime green")
frameTrabajadores.pack(expand=True,fill="both")
#
lbl_trabjadores = Label(frameTrabajadores,text="Registrar trabajadores", bg="yellow")
lbl_trabjadores.place(x=10,y=10,width=640,height=20)
#
lbl_rut = Label(frameTrabajadores, text="Rut:", bg="yellow", anchor="w")
lbl_rut.place(x=10,y=40,width=120,height=20)
txt_rut = Entry(frameTrabajadores)
txt_rut.place(x=140,y=40,width=120,height=20)
#
lbl_nombres = Label(frameTrabajadores, text="Nombres:", bg="yellow", anchor="w")
lbl_nombres.place(x=10,y=70,width=120,height=20)
txt_primerNombre = Entry(frameTrabajadores)
txt_primerNombre.place(x=140,y=70,width=120,height=20)
txt_segundoNombre = Entry(frameTrabajadores)
txt_segundoNombre.place(x=270,y=70,width=120,height=20)
#
lbl_apellidos = Label(frameTrabajadores, text="Apellidos:", bg="yellow", anchor="w")
lbl_apellidos.place(x=10,y=100,width=120,height=20)
txt_primerApellido = Entry(frameTrabajadores)
txt_primerApellido.place(x=140,y=100,width=120,height=20)
txt_segundoApellido = Entry(frameTrabajadores)
txt_segundoApellido.place(x=270,y=100,width=120,height=20)
#
lbl_fechaNacimiento = Label(frameTrabajadores, text="Fecha nacimiento:", bg="yellow", anchor="w")
lbl_fechaNacimiento.place(x=10,y=130,width=120,height=20)
txt_fechaNacimiento = Entry(frameTrabajadores)
txt_fechaNacimiento.place(x=140,y=130,width=120,height=20)
#
lbl_sexo = Label(frameTrabajadores, text="Sexo:", bg="yellow", anchor="w")
lbl_sexo.place(x=270,y=130,width=120,height=20)
txt_sexo = Entry(frameTrabajadores)
txt_sexo.place(x=400,y=130,width=120,height=20)
#
lbl_direccion = Label(frameTrabajadores, text="Direccion:", bg="yellow", anchor="w")
lbl_direccion.place(x=10,y=160,width=120,height=20)
txt_direccion = Entry(frameTrabajadores)
txt_direccion.place(x=140,y=160,width=250,height=20)
#
lbl_telefono = Label(frameTrabajadores, text="Telefono:", bg="yellow", anchor="w")
lbl_telefono.place(x=400,y=160,width=120,height=20)
txt_telefono = Entry(frameTrabajadores)
txt_telefono.place(x=530,y=160,width=120,height=20)
#
lbl_cargo = Label(frameTrabajadores, text="Cargo:", bg="yellow", anchor="w")
lbl_cargo.place(x=400,y=70,width=120,height=20) 
txt_cargo = Entry(frameTrabajadores)
txt_cargo.place(x=530,y=70,width=120,height=20)
#
lbl_departamento = Label(frameTrabajadores, text="Departamento:", bg="yellow", anchor="w")
lbl_departamento.place(x=400,y=100,width=120,height=20)
txt_departamento = Entry(frameTrabajadores)
txt_departamento.place(x=530,y=100,width=120,height=20)
#
lbl_rol = Label(frameTrabajadores, text="Rol:", bg="yellow", anchor="w")
lbl_rol.place(x=270,y=40,width=120,height=20)
variable = StringVar(frameTrabajadores)
variable.set("TJ") # default value
opt_rol = OptionMenu(frameTrabajadores,variable,"RH","TJ","JR")
opt_rol.place(x=400,y=40,width=120,height=20)
#
lbl_id = Label(frameTrabajadores,text="Id:", bg="yellow", anchor="w")
lbl_id.place(x=270,y=190,width=120,height=20)
txt_id = Entry(frameTrabajadores)
txt_id.place(x=400,y=190,width=120,height=20)
btn_id= Button(frameTrabajadores,text="Generar Id:",command=generarId)
btn_id.place(x=530,y=190,width=120,height=20)

#
btn_registrar = Button(frameTrabajadores,text="Registrar",command=obtenerTrabajador)
btn_registrar.place(x=140,y=190,width=120,height=20)
# X pocision horizontal 
# Y pocision vertical

"""CREATE TABLE `rrhh`.`personas` (
    `rut`               VARCHAR(10) NOT NULL ,
    `primer_nombre`     VARCHAR(50) NOT NULL , 
    `segundo_nombre`    VARCHAR(50) NULL , 
    `primer_apellido`   VARCHAR(50) NOT NULL , 
    `segundo_apellido`  VARCHAR(50) NULL , 
    `fecha_nacimiento`  DATE NOT NULL ,
    `sexo`              VARCHAR(1)  NOT NULL ,
    PRIMARY KEY (`rut`)
) ENGINE = InnoDB;

CREATE TABLE `rrhh`.`trabajadores` (
    `rut`               VARCHAR(10) NOT NULL ,
    `id_trabajador`     INT NOT NULL ,
    `estado`            VARCHAR(10) NOT NULL ,
    `telefono`          VARCHAR(15) ,
    `direccion`         VARCHAR(100) NOT NULL ,
    `rol`               VARCHAR(15) NOT NULL ,
    `clave`             VARCHAR(100) NOT NULL ,
    `fecha_ingreso`     DATE NOT NULL ,
    `fecha_inactividad` DATE NULL ,
    `id_laborales`      INT NOT NULL ,
    `id_cargo`          INT NOT NULL  ,
    PRIMARY KEY (`id_trabajador`)
) ENGINE = InnoDB;"""

vent.mainloop()