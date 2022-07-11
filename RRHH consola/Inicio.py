from funcionesSql import FxSql
from menus import Menu

sesion = (False,None)

def iniciarSesion():
    print ("*** RRHH ***")
    user = str(input ("Ingrese usuario: "))
    password = str(input ("Ingese su clave: "))
    rol = FxSql.validarClave(user, password)
    (rol, user)
    return (rol, user)

sesion = iniciarSesion()
if sesion[0] == False:
    print ("Usuario o contraseña incorrecto")
else:
    print ("Incio de sesion correcto")
    print ("Bienvenido",sesion[1],sesion[0])
    if sesion[0] == "JR":
        Menu.menuJR(sesion[1])
    if sesion[0] == "RH":
        Menu.menuRH(sesion[1])
    if sesion[0] == "TJ":
        Menu.menuTJ(sesion[1])

print ("Hasta luego :D")