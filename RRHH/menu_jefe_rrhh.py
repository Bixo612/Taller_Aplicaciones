from tkinter import *

vent = Tk()
vent.title("Inicio")
vent.geometry("500x250")

# defincion de elementos
lbl_bienvenido          = Label(vent,text="Bienvenido",bg="yellow")
btn_agregarIdLaboral    = Button(vent,text="Agregar Id laboral")
btn_agregarCargo        = Button(vent,text="Agregar cargo")
btn_agregarTrabajador   = Button(vent,text="Agregar Trabajador") 
btn_listarPorTrabajador = Button(vent,text="Lista de Trabajadores")
btn_listarPorCargo      = Button(vent,text="Listar por cargos")
btn_modificarContactos  = Button(vent,text="Contactos de emergencia")
btn_modificarCargas     = Button(vent,text="Cargas familiares")
btn_modifcarDatos       = Button(vent,text="Modificar datos")

# pocision de elementos
lbl_bienvenido.grid(row=0,column=1,padx=2,pady=2)
btn_agregarIdLaboral.grid(row=1,column=0,padx=2,pady=2)
btn_agregarCargo.grid(row=1,column=1,padx=2,pady=2)        
btn_agregarTrabajador.grid(row=1,column=2,padx=2,pady=2)   
btn_listarPorTrabajador.grid(row=2,column=0,padx=2,pady=2) 
btn_listarPorCargo.grid(row=2,column=1,padx=2,pady=2)      
btn_modificarContactos.grid(row=2,column=2,padx=2,pady=2)  
btn_modificarCargas.grid(row=3,column=0,padx=2,pady=2)    
btn_modifcarDatos.grid(row=3,column=1,padx=2,pady=2) 

vent.mainloop()

