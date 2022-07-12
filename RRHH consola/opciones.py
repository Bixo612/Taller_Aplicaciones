from datetime import date
from funcionesSql import FxSql
from validaciones import Val


class Opciones ():

    def editarPerfil(id):
        print("Configuración de perfil")
        exit = True
        while exit:
            print("0 Salir")
            print("1 Actualizar direccion")
            print("2 Actualizar telefono")
            print("3 Actualizar nombre")
            opcion = input("--Ingrese una opcion")
            if opcion == "1":
                direccion = input("--Ingrese la nueva direccion: ")
                FxSql.actualizarDireccion(direccion,id)
            if opcion == "2":
                telefono = input("--Indique el telefono: ")
                FxSql.actualizarTelefono(telefono,id)
            if opcion == "3":
                primerNombre    = input("--Ingrese el primer nombre: ")
                segundoNombre   = input("--Ingrese el segundo nombre: ")
                primerApellido  = input("--Ingrese el primer apellido: ")
                segundoApellido = input("--Ingrese el segundo apellido: ")
                FxSql.actualizarNombre(primerNombre,segundoNombre,primerApellido,segundoApellido,id)
            if opcion == "0":
                exit = False


    def gestionTrabajadores(id):
        print("Gestor de trabajadores")
        exit = True
        while exit:
            print("0 Salir")
            print("1 Listar Trabajadores")
            print("2 Buscar Trabajador")
            print("3 Agregar Trabajador")
            print("4 Moficar cargo de un trabajador")
            print("5 Modificar Departamento de un trabajador")
            print("6 listar cargos y departamentos")
            opcion = input("--Ingrese una opcion: ")
            if opcion == "1":
                for x in FxSql.listarTrabajadores():
                    print (x)
            if opcion == "2":
                buscar = input("--Ingrese el id a buscar: ")
                print(FxSql.consultarPerfil(buscar))
            if opcion == "4":
                id_trabajador   = input("--Ingrese el id del trabajador: ")
                cargo           = input("--Ingrese el nuevo cargo: ")
                FxSql.modificarCargo(id_trabajador,cargo)
            if opcion == "5":
                id_trabajador   = input("--Ingrese el id del trabajador: ")
                departamento    = input("--Ingrse el nuevo departamento: ")
                FxSql.modificarDepartamento(id_trabajador,departamento)
            if opcion == "6":
                print("---CARGOS---")
                for x in FxSql.listarCargos():
                    print(x)
                print("---DEPARTAMENTOS---")
                for y in FxSql.listarDepartamenos():
                    print(y)
            if opcion == "3":
                rut             = input("--Ingrese el rut: ")
                if FxSql.existeRutEnTrbajadores(rut):
                    print("¡El rut ya esta registrado")
                else:
                    primerNombre    = input("--Ingrese el primer nombre: ")
                    segundoNombre   = input("--Ingrese el segundo nombre: ")
                    primerApellido  = input("--Ingrese el primer apellido: ")
                    segundoApellido = input("--Ingrese el segundo apellido: ")
                    fechaNacimiento = input("--Ingrese la fecha de nacimiento (XXXX-XX-XX): ")
                    sexo            = Val.validarSexo()
                    #
                    id_trabajador   = input("--Indique el id: ")
                    telefono        = input("--Indique el telefono: ")
                    direccion       = input("--Indique la direccion: ")
                    rol             = input("--Indique el rol: ")
                    clave           = input("--Indique la clave: ")
                    cargo           = input("--Indique el cargo: ")
                    departamento    = input("--Indique el departamento: ")
                    #
                    FxSql.agregarPersona(rut, primerNombre, segundoNombre, primerApellido, segundoApellido, fechaNacimiento, sexo)
                    FxSql.agregarTrabajador(rut, id_trabajador,"Activo", telefono, direccion, rol, clave,date.today(),departamento,cargo)
            if opcion == "0":
                exit = False
        
    def gestionDepartamentosCargos(id):
        print("Gestor de contactos de cargos y departamentos")
        exit = True
        while exit:
            print("0 Salir")
            print("1 Listar cargos")
            print("2 Listar departamentos")
            print("3 Agregar cargo")
            print("4 Agregar departamento")
            print("5 Eliminar cargo")
            print("6 Eliminar Departamento")
            opcion = input("--Ingrese una opcion: ")
            if opcion == "1":
                for x in FxSql.listarCargos():
                    print(x)
            if opcion == "2":
                for y in FxSql.listarDepartamenos():
                    print(y)
            if opcion == "3":
                id_cargo    = input("--Ingrese el id del cargo: ")
                nombre      = input("--Ingrese el nombre del cargo: ")
                FxSql.agregarCargo(id_cargo, nombre)
            if opcion == "4":
                id_departamento     = input("--Ingrese el id del departamento: ")
                departamento        = input("--Ingrese el nombre del departamento: ")
                area                = input("--Ingrese el area: ")
                FxSql.agregarDepartamento(id_departamento,area,departamento)
            if opcion == "5":
                id_cargo = input("--Ingrese el id del cargo: ")
                FxSql.borrarCargo(id_cargo)
            if opcion == "6":
                id_cargo = input("--Ingrese el id del departamento: ")
                FxSql.borrarDepartamento(id_cargo)
            if opcion == "0":
                exit = False

    def gestionCargasContactos(id):
        print("Gestor de contactos de emergencia y cargas laborales")
        exit = True
        while exit:
            print("0 Salir")
            print("1 Agregar contacto de emergencia")
            print("2 agregar carga laboral")
            print("3 listar cargas y contactos de emergencia")
            print("4 Eliminar carga")
            print("5 Eliminar contacto de emergencia")
            opcion = input("--Ingrese una opcion")
            if opcion == "1":
                print("A continuacion ingrese los datos del contacto de emergencia")
                nombre      = input("--Ingrese el nombre: ")
                relacion    = input("--Indicque la relacion: ")
                numero1     = input("--Indique el telefono movil: ")
                numero2     = input("--Indique el telefono fijo: ")
                FxSql.agregarContactos(nombre, relacion, numero1, numero2, id)
            if opcion == "2":
                rut             = input("--Ingrese el rut: ")
                primerNombre    = input("--Ingrese el primer nombre: ")
                segundoNombre   = input("--Ingrese el segundo nombre: ")
                primerApellido  = input("--Ingrese el primer apellido: ")
                segundoApellido = input("--Ingrese el segundo apellido: ")
                fechaNacimiento = input("--Ingrese la fecha de nacimiento (XXXX-XX-XX): ")
                sexo            = Val.validarSexo()
                relacion        = input("--Indique la relacion o parentesco: ")
                FxSql.agregarPersona(rut, primerNombre, segundoNombre, primerApellido, segundoApellido, fechaNacimiento, sexo)
                FxSql.agregarCargas(rut, id, relacion)
            if opcion == "3":
                print("Cargas:")
                for x in (FxSql.listarCargas(id)):
                    print(x)
                print("Contactos de emergencia:")
                for y in (FxSql.listarContactos(id)):
                    print(y)
            if opcion == "4":
                rut = input("--Indique el rut de la carga que desea eliminar: ")
                FxSql.eliminarCarga(rut, id)
            if opcion == "5":
                nombre = input(
                    "Indique el nombre del contacto que desea eliminar: ")
                FxSql.eliminarContactoNombre(nombre, id)
            if opcion == "0":
                exit = False
