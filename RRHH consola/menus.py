from funcionesSql import FxSql
from opciones import Opciones

class Menu():

    def menuJR(id):
        print("Menu de jefe de recursos humanos")
        exit = True
        while exit:
            print("0 Salir")
            print("1 Consultar perfil")
            print("2 Gestor de cargas y contactos de emergencia")
            print("3 Gestor de cargos y departamentos")
            print("4 Gestor de trabajadores")
            print("5 Editar perfil")
            print("6 Gestor de trabajadores avanzados")
            opcion = input("--Ingrese una opcion: ")
            if opcion == "1":
                print(FxSql.consultarPerfil(id))
            if opcion == "2":
                Opciones.gestionCargasContactos(id)
            if opcion == "3":
                Opciones.gestionDepartamentosCargos(id)
            if opcion == "4":
                Opciones.gestionTrabajadores(id)
            if opcion == "5":
                Opciones.editarPerfil(id)
            if opcion == "6":
                Opciones.gestionTrabajadoresAvanzado(id)
            if opcion == "0":
                exit = False

    def menuRH(id):
        print("Menu de personal de recursos humanos")
        exit = True
        while exit:
            print("0 Salir")
            print("1 Consultar perfil")
            print("2 Gestor de cargas y contactos de emergencia")
            print("3 Gestor de trabajadores")
            print("4 Editar perfil")
            opcion = input("--Ingrese una opcion: ")
            if opcion == "1":
                print(FxSql.consultarPerfil(id))
            if opcion == "2":
                Opciones.gestionCargasContactos(id)
            if opcion == "3":
                Opciones.gestionTrabajadores(id)
            if opcion == "4":
                Opciones.editarPerfil(id)
            if opcion == "0":
                exit = False

    def menuTJ(id):
        print("Menu de trabajadores")
        exit = True
        while exit:
            print("0 Salir")
            print("1 Consultar perfil")
            print("2 Gestor de cargas y contactos de emergencia")
            print("3 Editar perfil")
            opcion = input("--Ingrese una opcion: ")
            if opcion == "1":
                print(FxSql.consultarPerfil(id))
            if opcion == "2":
                Opciones.gestionCargasContactos(id)
            if opcion == "3":
                Opciones.editarPerfil(id)
            if opcion == "0":
                exit = False

    def menuROOT(id):
        print("Menu de jefe de recursos humanos")
        exit = True
        while exit:
            print("0 Salir")
            print("1 Gestor de cargos y departamentos")
            print("2 Gestor de trabajadores")
            print("3 Gestor de trabajadores avanzados")
            opcion = input("--Ingrese una opcion: ")
            if opcion == "1":
                Opciones.gestionDepartamentosCargos(id)
            if opcion == "2":
                Opciones.gestionTrabajadores(id)
            if opcion == "3":
                Opciones.gestionTrabajadoresAvanzado(id)
            if opcion == "0":
                exit = False