from funcionesSql import FxSql

class Fts():

    def consultarPerfil(x):
        if x == []:
            print ("¡No existe el trbajador!")
        else:
            x = x[0]
            print ("Nombre:",x[2],"| Rut:",x[1],"| Fecha Nacimiento:",x[3])
            print ("Telefono:",x[5],"| Direccion:",x[6],"| Sexo:",x[4])
            print ("Cargo:",FxSql.cargXid(x[9]),"| Departamento:",FxSql.depaXid(x[8]),"| Area:",FxSql.areaXid(x[8]))

    def formatoBusquedaTrabajador(x):
        if x == []:
            print ("¡No existe el trbajador!")
        else:
            x = x[0]
            print ("Id:",x[0],"| Rut:",x[1],"| Cargo:",FxSql.cargXid(x[9]),"| Departamento:",FxSql.cargXid(x[9]),"| Area:",FxSql.areaXid(x[8]))
            print ("Fecha Ingreso:",x[7],"| Fecha Inactividad:",x[10])
            print ("Nombre completo:",x[2])

    def formatoTrabajadores(trabajadores):
        if trabajadores == []:
            print ("¡No hay trabajadores!")
        else:
            print (" Rut        |  Id  | Sexo | Cargo               | Departamento	      | Nombre")
            for x in trabajadores:
                print ("{:^12}|{:^6}|{:^6}| {:<20}| {:<20}| {}".format(x[1],x[0], x[4], FxSql.cargXid(x[9]),FxSql.depaXid(x[8]), x[2])) 

    def formatoTrabajadoresFiltro(trabajadores):
        if trabajadores == []:
            print ("¡No hay trabajadores!")
        else:
            print (" Rut        |  Id  | Sexo | Cargo               | Departamento	      | Area                 | Estado   | Nombre")
            for x in trabajadores:
                print ( "{:^12}|{:^6}|{:^6}| {:<20}| {:<20}| {:<20} | {:<9}| {}".format(x[1],x[0],x[4], FxSql.cargXid(x[9]),FxSql.depaXid(x[8]),FxSql.areaXid(x[8]),x[10],x[2]))

    def formatoCargos(cargos):
        if cargos == []:
            print ("¡No hay cargos!")
        else:
            print (" Id   | Cargo")
            for x in cargos:
                print ("{:^6}| {}".format(x[0], x[1]))

    def formatoDepartamentos(departamentos):
        if departamentos == []:
            print ("¡No hay departamentos!")
        else:
            print (" Id   | Departamento         | Area")
            for x in departamentos:
                print ("{:^6}| {:<20} | {}".format(x[0], x[1], x[2]))

    def formatoCargas(cargas):
        if cargas == []:
            print ("¡No hay cargas!")
        else:
            print (" Fecha Nacimiento | Rut        | Sexo | Nombre")
            for x in cargas:
                print (" {}       |{:^12}|{:^6}| {} ".format(x[2], x[0], x[3],  x[1]))

    def formatoContactos(contactos):
        if contactos == []:
            print ("¡No hay contactos!")
        else:
            print ("Nombre          | Relacion       | Telefono Movil | Telefono Fijo")
            for x  in contactos:
                print (" {:<15}| {:<15}| {:<15}| {}S".format(x[0], x[1], x[2],x[3]))

