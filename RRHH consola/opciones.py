from funcionesSql import FxSql
from validaciones import Val

class Opciones ():

    def gestionTrabajadoresAvanzado(id):
        print("Gestor de trabajadores avanzado")
        exit = True
        while exit:
            print("0 Salir")
            print("1 Cambiar el estado de un trabajador")
            print("2 Listar trabajador por cargo")
            print("3 Listar trabajador por departamento")
            print("4 Listar trabajador por sexo")
            opcion = input("--Ingrese una opcion: ")
            if opcion == "1":
                id_trabajador = Val.validarInt("--Ingrese el id del trabajador: ")
                FxSql.cambiarEstado(id_trabajador)
            if opcion == "2":
                cargo = Val.validarInt("--Ingrese el cargo: ")
                for x in FxSql.listarTrabajadoresCargo(cargo):
                    print(x)
            if opcion == "3":
                departamento = Val.validarInt("--Ingrese el departamento: ")
                for y in FxSql.listarTrabajadoresDepartamento(departamento):
                    print(y)
            if opcion == "4":
                sexo = Val.validarSexo()
                for z in FxSql.listarTrabajadoresSexo(sexo):
                    print(z)
            if opcion == "0":
                exit = False

    def editarPerfil(id):
        print("Configuración de perfil")
        exit = True
        while exit:
            print("0 Salir")
            print("1 Actualizar direccion")
            print("2 Actualizar telefono")
            print("3 Actualizar nombre")
            print("4 Cambiar clave")
            opcion = input("--Ingrese una opcion: ")
            if opcion == "1":
                direccion = Val.validarString("--Ingrese la nueva direccion: ")
                FxSql.actualizarDireccion(direccion,id)
            if opcion == "2":
                telefono = Val.validarString("--Indique el telefono: ")
                FxSql.actualizarTelefono(telefono,id)
            if opcion == "3":
                primerNombre    = Val.validarString("--Ingrese el primer nombre: ")
                segundoNombre   = Val.validarString("--Ingrese el segundo nombre: ")
                primerApellido  = Val.validarString("--Ingrese el primer apellido: ")
                segundoApellido = Val.validarString("--Ingrese el segundo apellido: ")
                FxSql.actualizarNombre(primerNombre,segundoNombre,primerApellido,segundoApellido,id)
            if opcion == "4":
                claveActual = Val.validarString("--Ingrese su clave actual: ")
                if FxSql.validarClave(id,claveActual) == False:
                    print ("Clave incorrecta")
                else:
                    claveNueva = Val.validarString("--Ingrese su nueva clave: ")
                    FxSql.actualizarClave(id,claveNueva)
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
            print("7 Restablecer Clave")
            opcion = input("--Ingrese una opcion: ")
            if opcion == "1":
                for x in FxSql.listarTrabajadores():
                    print (x)
            if opcion == "2":
                buscar = Val.validarInt("--Ingrese el id a buscar: ")
                print(FxSql.consultarPerfil(buscar))
            if opcion == "4":
                id_trabajador   = Val.validarInt("--Ingrese el id del trabajador: ")
                cargo           = Val.validarString("--Ingrese el nuevo cargo: ")
                FxSql.modificarCargo(id_trabajador,cargo)
            if opcion == "5":
                id_trabajador   = Val.validarInt("--Ingrese el id del trabajador: ")
                departamento    = Val.validarString("--Ingrse el nuevo departamento: ")
                FxSql.modificarDepartamento(id_trabajador,departamento)
            if opcion == "7":
                id_trabajador = Val.validarInt("--Ingrese la id del trabajador: ")
                claveNueva = Val.generarClave()
                FxSql.actualizarClave(id,claveNueva)
            if opcion == "6":
                print("---CARGOS---")
                for x in FxSql.listarCargos():
                    print(x)
                print("---DEPARTAMENTOS---")
                for y in FxSql.listarDepartamenos():
                    print(y)
            if opcion == "3":
                rut             = Val.validarRut("--Ingrese el rut: ")
                if FxSql.existeRutEnTrbajadores(rut):
                    print("¡El rut ya esta registrado")
                else:
                    primerNombre    = Val.validarString("--Ingrese el primer nombre: ")
                    segundoNombre   = Val.validarString("--Ingrese el segundo nombre: ")
                    primerApellido  = Val.validarString("--Ingrese el primer apellido: ")
                    segundoApellido = Val.validarString("--Ingrese el segundo apellido: ")
                    fechaNacimiento = Val.validarFecha("--Ingrese la fecha de nacimiento (XXXX-XX-XX): ")
                    sexo            = Val.validarSexo()
                    #
                    id_trabajador   = Val.validarInt("--Indique el id: ")
                    telefono        = Val.validarInt("--Indique el telefono: ")
                    direccion       = Val.validarString("--Indique la direccion: ")
                    rol             = Val.validarRol()
                    cargo           = Val.validarInt("--Indique el cargo: ")
                    departamento    = Val.validarInt("--Indique el departamento: ")
                    fechaIngreso    = Val.validarInt("--Indique la fecha de ingreso (XXXX-XX-XX): ")
                    #
                    FxSql.agregarPersona(rut, primerNombre, segundoNombre, primerApellido, segundoApellido, fechaNacimiento, sexo)
                    FxSql.agregarTrabajador(rut, id_trabajador,"Activo", telefono, direccion, rol, "clave123",fechaIngreso,departamento,cargo)
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
            print("7 Editar Cargo")
            print("8 Editar Departamento")
            opcion = input("--Ingrese una opcion: ")
            if opcion == "1":
                for x in FxSql.listarCargos():
                    print(x)
            if opcion == "2":
                for y in FxSql.listarDepartamenos():
                    print(y)
            if opcion == "3":
                id_cargo    = Val.validarInt("--Ingrese el id del cargo: ")
                cargo       = Val.validarString("--Ingrese el nombre del cargo: ")
                FxSql.agregarCargo(id_cargo, cargo)
            if opcion == "4":
                id_departamento     = input("--Ingrese el id del departamento: ")
                departamento        = Val.validarString("--Ingrese el nombre del departamento: ")
                area                = Val.validarString("--Ingrese el area: ")
                FxSql.agregarDepartamento(id_departamento,area,departamento)
            if opcion == "5":
                id_cargo = Val.validarInt("--Ingrese el id del cargo: ")
                FxSql.borrarCargo(id_cargo)
            if opcion == "6":
                id_cargo = Val.validarInt("--Ingrese el id del departamento: ")
                FxSql.borrarDepartamento(id_cargo)
            if opcion == "0":
                exit = False

    def gestionCargasContactos(id):
        print("Gestor de contactos de emergencia y cargas laborales")
        exit = True
        while exit:
            print("0 Salir")
            print("1 Agregar contacto de emergencia")
            print("2 Agregar carga laboral")
            print("3 listar cargas y contactos de emergencia")
            print("4 Eliminar carga")
            print("5 Eliminar contacto de emergencia")
            opcion = input("--Ingrese una opcion: ")
            if opcion == "1":
                print("A continuacion ingrese los datos del contacto de emergencia")
                nombre      = Val.validarString("--Ingrese el nombre: ")
                relacion    = Val.validarString("--Indicque la relacion: ")
                numero1     = Val.validarInt("--Indique el telefono movil: ")
                numero2     = Val.validarInt("--Indique el telefono fijo: ")
                FxSql.agregarContactos(nombre, relacion, numero1, numero2, id)
            if opcion == "2":
                rut             = Val.validarRut("--Ingrese el rut: ")
                primerNombre    = Val.validarString("--Ingrese el primer nombre: ")
                segundoNombre   = Val.validarString("--Ingrese el segundo nombre: ")
                primerApellido  = Val.validarString("--Ingrese el primer apellido: ")
                segundoApellido = Val.validarString("--Ingrese el segundo apellido: ")
                fechaNacimiento = Val.validarFecha("--Ingrese la fecha de nacimiento (XXXX-XX-XX): ")
                sexo            = Val.validarSexo()
                relacion        = Val.validarString("--Indique la relacion o parentesco: ")
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
                rut = Val.validarRut("--Indique el rut de la carga que desea eliminar: ")
                FxSql.eliminarCarga(rut, id)
            if opcion == "5":
                nombre = Val.validarString("--Indique el nombre del contacto que desea eliminar: ")
                FxSql.eliminarContactoNombre(nombre, id)
            if opcion == "0":
                exit = False