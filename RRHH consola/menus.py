from funcionesSql import FxSql

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
    print (sesion)