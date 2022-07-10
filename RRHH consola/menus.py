from funcionesSql import FxSql
sesion = (False,None)

def iniciarSesion():
    print ("*** RRHH ***")
    user = str(input ("Ingrese usuario: "))
    password = str(input ("Ingese su clave: "))
    rol = FxSql.validarClave(user, password)
    (rol, user)
    return (rol, user)

def menuJR():
    print("Menu de personal de jefe de recursos humanos")
    exit = True
    while exit:
        opcion = input("Ingrese una opcion")
        if opcion == "0":
            exit = False

def menuRH():
    print("Menu de personal de recursos humanos")

def menuTJ():
    print("Menu de trabajadores")

sesion = iniciarSesion()
if sesion[0] == False:
    print ("Usuario o contraseña incorrecto")
else:
    print ("Incio de sesion correcto")
    print ("Bienvenido",sesion[1],sesion[0])
    if sesion[0] == "JR":
        menuJR()
    if sesion[0] == "RH":
        menuRH()
    if sesion[0] == "TJ":
        menuTJ()

print ("Hasta luego :D")