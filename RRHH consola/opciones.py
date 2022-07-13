from funcionesSql import FxSql
from validaciones import Val
from formatos import Fts


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
                id_trabajador = Val.validarInt(
                    "--Ingrese el id del trabajador: ")
                FxSql.cambiarEstado(id_trabajador)
            if opcion == "2":
                cargo = Val.validarInt("--Ingrese el cargo: ")
                Fts.formatoTrabajadoresFiltro(
                    FxSql.listarTrabajadoresCargo(cargo))
            if opcion == "3":
                departamento = Val.validarInt("--Ingrese el departamento: ")
                Fts.formatoTrabajadoresFiltro(
                    FxSql.listarTrabajadoresDepartamento(departamento))
            if opcion == "4":
                sexo = Val.validarSexo()
                Fts.formatoTrabajadoresFiltro(
                    FxSql.listarTrabajadoresSexo(sexo))
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
                FxSql.actualizarDireccion(direccion, id)
            if opcion == "2":
                telefono = Val.validarString("--Indique el telefono: ")
                FxSql.actualizarTelefono(telefono, id)
            if opcion == "3":
                primerNombre = Val.validarString(
                    "--Ingrese el primer nombre: ")
                segundoNombre = Val.validarString(
                    "--Ingrese el segundo nombre: ")
                primerApellido = Val.validarString(
                    "--Ingrese el primer apellido: ")
                segundoApellido = Val.validarString(
                    "--Ingrese el segundo apellido: ")
                FxSql.actualizarNombre(
                    primerNombre, segundoNombre, primerApellido, segundoApellido, id)
            if opcion == "4":
                claveActual = Val.validarString("--Ingrese su clave actual: ")
                if FxSql.validarClave(id, claveActual) == False:
                    print("Clave incorrecta")
                else:
                    claveNueva = Val.validarString(
                        "--Ingrese su nueva clave: ")
                    FxSql.actualizarClave(id, claveNueva)
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
            print("6 Listar cargos y departamentos")
            print("7 Restablecer Clave")
            opcion = input("--Ingrese una opcion: ")
            if opcion == "1":
                Fts.formatoTrabajadores(FxSql.listarTrabajadoresActivos())
            if opcion == "2":
                buscar = Val.validarInt("--Ingrese el id a buscar: ")
                Fts.formatoBusquedaTrabajador(FxSql.consultarPerfil(buscar))
            if opcion == "4":
                id_trabajador = Val.validarInt(
                    "--Ingrese el id del trabajador: ")
                cargo = Val.validarString("--Ingrese el nuevo cargo: ")
                FxSql.modificarCargo(id_trabajador, cargo)
            if opcion == "5":
                id_trabajador = Val.validarInt(
                    "--Ingrese el id del trabajador: ")
                departamento = Val.validarString(
                    "--Ingrse el nuevo departamento: ")
                FxSql.modificarDepartamento(id_trabajador, departamento)
            if opcion == "7":
                id_trabajador = Val.validarInt(
                    "--Ingrese la id del trabajador: ")
                claveNueva = Val.generarClave()
                FxSql.actualizarClave(id, claveNueva)
            if opcion == "6":
                print("---CARGOS---")
                Fts.formatoCargos(FxSql.listarCargos())
                print("---DEPARTAMENTOS---")
                Fts.formatoDepartamentos(FxSql.listarDepartamenos())
            if opcion == "3":
                rut = Val.validarRut("--Ingrese el rut: ")
                if FxSql.existeRutEnTrbajadores(rut):
                    print("¡El rut ya esta registrado")
                else:
                    primerNombre = Val.validarString(
                        "--Ingrese el primer nombre: ")
                    segundoNombre = Val.validarString(
                        "--Ingrese el segundo nombre: ")
                    primerApellido = Val.validarString(
                        "--Ingrese el primer apellido: ")
                    segundoApellido = Val.validarString(
                        "--Ingrese el segundo apellido: ")
                    fechaNacimiento = Val.validarFecha(
                        "--Ingrese la fecha de nacimiento (XXXX-XX-XX): ")
                    sexo = Val.validarSexo()
                    #
                    id_trabajador = Val.validarInt("--Indique el id: ")
                    telefono = Val.validarInt("--Indique el telefono: ")
                    direccion = Val.validarString("--Indique la direccion: ")
                    rol = Val.validarRol()
                    cargo = Val.validarInt("--Indique el cargo: ")
                    departamento = Val.validarInt(
                        "--Indique el departamento: ")
                    fechaIngreso = Val.validarFecha(
                        "--Indique la fecha de ingreso (XXXX-XX-XX): ")
                    #
                    FxSql.agregarPersona(rut, primerNombre, segundoNombre,
                                         primerApellido, segundoApellido, fechaNacimiento, sexo)
                    FxSql.agregarTrabajador(rut, id_trabajador, "Activo", telefono,
                                            direccion, rol, "clave123", fechaIngreso, departamento, cargo)
                    print("¡Se ha registado correctamente! y su clave es: clave123 ")
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
                Fts.formatoCargos(FxSql.listarCargos())
            if opcion == "2":
                Fts.formatoDepartamentos(FxSql.listarDepartamenos())
            if opcion == "3":
                id_cargo = Val.validarCargo()
                cargo = Val.validarString("--Ingrese el nombre del cargo: ")
                FxSql.agregarCargo(id_cargo, cargo)
            if opcion == "4":
                id_departamento = Val.validarDepartamento()
                departamento = Val.validarString(
                    "--Ingrese el nombre del departamento: ")
                area = Val.validarString("--Ingrese el area: ")
                FxSql.agregarDepartamento(id_departamento, area, departamento)
            if opcion == "5":
                id_cargo = Val.validarInt("--Ingrese el id del cargo: ")
                if Val.cargoVacio(id_cargo):
                    FxSql.borrarCargo(id_cargo)
                else:
                    print("¡Existen trabajadores con ese cargo asingado!")
            if opcion == "6":
                id_departamento = Val.validarInt(
                    "--Ingrese el id del departamento: ")
                if Val.departamentoVacio(id_departamento):
                    FxSql.borrarDepartamento(id_departamento)
                else:
                    print("¡Existen trabajadores con ese departamento asingado!")
            if opcion == "7":
                id_cargo = Val.validarInt("--Ingrese el id del cargo: ")
                if FxSql.existeCago(id_cargo):
                    cargo = Val.validarString(
                        "--Ingrese el nuevo nombre del cargo:")
                    FxSql.modificarCargo(id_cargo, cargo)
                else:
                    print("¡No existe el cargo!")
            if opcion == "8":
                id_departamento = Val.validarInt("--Ingrese el id del cargo: ")
                if FxSql.existeDepartamento(id_departamento):
                    departamento = Val.validarString(
                        "--Ingrese el nuevo nombre del departamento: ")
                    area = Val.validarString(
                        "--Ingrese la nueva area del departamento: ")
                    FxSql.modificarDepartamento(
                        id_departamento, area, departamento)
                else:
                    print("¡No existe el departamento!")
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
                nombre = Val.validarString("--Ingrese el nombre: ")
                relacion = Val.validarString("--Indicque la relacion: ")
                numero1 = Val.validarInt("--Indique el telefono movil: ")
                numero2 = Val.validarInt("--Indique el telefono fijo: ")
                FxSql.agregarContactos(nombre, relacion, numero1, numero2, id)
            if opcion == "2":
                rut = Val.validarRut("--Ingrese el rut: ")
                if FxSql.existeRutEnCargas(rut):
                    print("¡El rut ya esta registrado")
                else:
                    primerNombre = Val.validarString(
                        "--Ingrese el primer nombre: ")
                    segundoNombre = Val.validarString(
                        "--Ingrese el segundo nombre: ")
                    primerApellido = Val.validarString(
                        "--Ingrese el primer apellido: ")
                    segundoApellido = Val.validarString(
                        "--Ingrese el segundo apellido: ")
                    fechaNacimiento = Val.validarFecha(
                        "--Ingrese la fecha de nacimiento (XXXX-XX-XX): ")
                    sexo = Val.validarSexo()
                    relacion = Val.validarString(
                        "--Indique la relacion o parentesco: ")
                    FxSql.agregarPersona(rut, primerNombre, segundoNombre,
                                         primerApellido, segundoApellido, fechaNacimiento, sexo)
                    FxSql.agregarCargas(rut, id, relacion)
            if opcion == "3":
                print("Cargas:")
                Fts.formatoCargas(FxSql.listarCargas(id))
                print("Contactos de emergencia:")
                Fts.formatoContactos(FxSql.listarContactos(id))
            if opcion == "4":
                rut = Val.validarRut(
                    "--Indique el rut de la carga que desea eliminar: ")
                FxSql.eliminarCarga(rut, id)
            if opcion == "5":
                nombre = Val.validarString(
                    "--Indique el nombre del contacto que desea eliminar: ")
                FxSql.eliminarContactoNombre(nombre, id)
            if opcion == "0":
                exit = False
