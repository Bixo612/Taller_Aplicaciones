from tkinter import Tk, Label, Button

def mensaje ():
    print ("Mensaje del boton")

ventana = Tk()
ventana.geometry("400x400")
ventana.title("Ventana hola mundo")

lbl = Label(ventana,text='Este es un [Label] tkinter')
lbl.pack()

btn = Button(ventana, text='Presiona este [Button] para mensaje',command=mensaje,fg="red",bg="blue")
# Otras formas de pasarle armgumentos
# btn.config(fg="red",bg="green")
# btn["fg"] = "green"
# btn["bg"] = "black"
btn.pack()

ventana.mainloop()

