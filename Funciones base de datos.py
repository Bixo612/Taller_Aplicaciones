import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rrhh"
    )

cursor = con.cursor()

def agregarPersona(rut,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,fecha_nacimiento,sexo):
        sql = ( "Insert into personas values "
                "(rut, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, sexo) "
                "values %s,%s,%s,%s,%s,%s,%s")
        var = (rut,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,fecha_nacimiento,sexo,)
        cursor.execute(sql,var)

agregarPersona("13524625-K","Felipe","Andres","Soto","Muñoz","1995-06-16","M")

