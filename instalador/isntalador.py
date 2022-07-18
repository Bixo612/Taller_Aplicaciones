import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = con.cursor()

cursor.execute("show databases")

existe = False

for x in cursor:
    if x == ('rrhh',):
        existe = True
if existe:
    print ("La base de datos ya existe")
else:
    cursor.execute("CREATE DATABASE rrhh")
    print ("Se ha creado la base de datos")

    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="RRHH"
    )

    with open(r'C:\Users\vicen\Github_b\Taller_Aplicaciones\instalador\TallerDeAplicaciones.sql', "r",encoding = "utf-8") as f:
        with con.cursor() as cursor:
            cursor.execute(f.read(), multi=True)
        con.commit()