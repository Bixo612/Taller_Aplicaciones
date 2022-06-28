import mysql.connector
from datetime import date

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rrhh"
    )

cursor = con.cursor()

class FxSql():

    # Funciones de agregacion

    def agregarPersona(rut,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,fecha_nacimiento,sexo):
        sql = "INSERT INTO personas (rut,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,fecha_nacimiento,sexo) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (rut,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,fecha_nacimiento,sexo,)
        cursor.execute(sql, val)
        con.commit() 

    def agregarCargo(id_cargo,nombre_cargo):
        sql = "INSERT INTO cargos (id_cargo,nombre_cargo) VALUES (%s,%s)"
        val = (id_cargo,nombre_cargo,)
        cursor.execute(sql,val)
        con.commit()

    def agregarDatosLaborales(id_labores,area,departamento):
        sql = "INSERT INTO laborales (id_labores,area,departamento) VALUES (%s,%s,%s)"
        val = (id_labores,area,departamento,)
        cursor.execute(sql,val)
        con.commit()

    def agregarTrabajador(rut,id_trabajador,estado,telefono,direccion,rol,clave,fecha_ingreso,fecha_inactividad,id_laborales,id_cargo):
        sql = "INSERT INTO trabajadores (rut,id_trabajador,estado,telefono,direccion,rol,clave,fecha_ingreso,fecha_inactividad,id_laborales,id_cargo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
        val = (rut,id_trabajador,estado,telefono,direccion,rol,clave,fecha_ingreso,fecha_inactividad,id_laborales,id_cargo,)
        cursor.execute(sql,val)
        con.commit()

    def agregarCargas(rut,id_trabajador,relacion):
        sql = "INSERT INTO cargas (rut,id_trabajador,relacion) VALUES (%s,%s,%s)"
        val = (rut,id_trabajador,relacion,)
        cursor.execute(sql,val)
        con.commit()

    def agregarContactos(nombre,relacion,numero1,numero2,id_trabajador):
        sql = "INSERT INTO contactos (nombre,relacion,numero1,numero2,id_trabajador) VALUES (%s,%s,%s,%s,%s)"
        val = (nombre,relacion,numero1,numero2,id_trabajador,)
        cursor.execute(sql,val)
        con.commit()

    # Funcionees de consulta

    def listarTrabajadores():
        sql = "SELECT * FROM trabajadores"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        return resultado

    def consultarPorIdYClave(id_trabajador,clave):
        pass


# FxSql.agregarTrabajador("19360397-K",150,"Activo",951457895,"Isla Guafo 8934","usuario","pikachu",date.today(),None,15,1)
# FxSql.agregarPersona("19360397-K","Alan","Felipe","Soto","Campos","1996-05-12","M")
# today = date.today()
# print(today)

print(FxSql.listarTrabajadores())