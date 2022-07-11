from funcionesSql import FxSql
from opciones import Opciones

class Menu():

    def menuJR(id):
        print("Menu de personal de jefe de recursos humanos")
        exit = True
        while exit:
            print("0 Salir")
            print("1 Consultar perfil")
            print("2 Gestor de cargas y contactos de emergencia")
            print("3 Gestor de cargos y departamentos")
            print("4 Gestor de trabajadores")
            opcion = input("Ingrese una opcion: ")
            if opcion == "1":
                print(FxSql.consultarPerfil(id))
            if opcion == "2":
                Opciones.gestionCargasContactos(id)
            if opcion == "3":
                Opciones.gestionDepartamentosCargos()
            if opcion == "4":
                Opciones.gestionTrabajadores()
            
            if opcion == "0":
                exit = False

    def menuRH():
       print("Menu de personal de recursos humanos")

    def menuTJ():
        print("Menu de trabajadores")
