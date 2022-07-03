from cgitb import text
from tkinter import *

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
txt_rol = OptionMenu(frameTrabajadores,variable,"RH","TJ","JR")
txt_rol.place(x=400,y=40,width=120,height=20)
#


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