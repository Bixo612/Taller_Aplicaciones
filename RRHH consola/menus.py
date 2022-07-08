from funcionesSql import FxSql

secion = (False,None)

def iniciarSesion():
    print ("*** RRHH ***")
    user = str(input ("Ingrese usuario: "))
    password = str(input ("Ingese su clave: "))
    rol = FxSql.validarClave(user, password)
    (rol, user)
    return (rol, user)

secion = iniciarSesion()
if secion[0] == False:
    print ("Usuario o contraseña incorrecto")
else:
    print ("Inciio de secion correcto")
    print (secion)