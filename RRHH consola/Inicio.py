from funcionesSql import FxSql
from menus import Menu

sesion = (False,None)

def iniciarSesion():
    print ("*** RRHH ***")
    user = str(input ("--Ingrese usuario: "))
    password = str(input ("--Ingrese su clave: "))
    rol = FxSql.validarClave(user, password)
    (rol, user)
    return (rol, user)

sesion = iniciarSesion()
if sesion[0] == False:
    print ("Usuario o contraseña incorrecto")
else:
    print ("Inicio de sesion correcto")
    print ("Bienvenido",sesion[1],sesion[0])
    if sesion[0] == "JR":
        Menu.menuJR(sesion[1])
    if sesion[0] == "RH":
        Menu.menuRH(sesion[1])
    if sesion[0] == "TJ":
        Menu.menuTJ(sesion[1])
    if sesion[0] == "root":
        Menu.menuROOT("root")

print ("Hasta luego :")