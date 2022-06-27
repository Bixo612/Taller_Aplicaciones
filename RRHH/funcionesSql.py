import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rrhh"
    )

cursor = con.cursor()

class FxSql():

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

                
    
FxSql.agregarPersona("19360397-K","Alan","Felipe","Soto","Campos","1996-05-12","M")
