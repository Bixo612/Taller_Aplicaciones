class Val():

    def validarSexo():
        sexo = None
        while sexo == None:
            sexo = input("Indique el sexo (M-F): ")
            if sexo == "M" or sexo == "F":
                return sexo
            else:
                sexo = None

    def validarRol():
        rol = None
        while rol == None:
            rol = input("Indique el rol (JR-RH-TJ): ")
            if rol == "JR" or rol == "RH" or rol == "TJ":
                return rol
            else:
                rol = None

    def validarString(pregunta):
        string = None
        while string == None:
            string = input(pregunta)
            if string == "" or string == None:
                string = None
            else:
                return string

    def validarRut(pregunta):
        rut = None
        while rut == None:
            rut = input(pregunta)
            if len(rut) == 0 or len(rut) > 10: 
                rut = None
            else:
                return rut

    def validarFecha(pregunta):
        fecha = None
        while fecha == None:
            fecha = input(pregunta)
            if len(fecha) != 10:
                fecha = None
            else:
                if fecha[4] != "-" and fecha[7] != "-":
                    fecha = None
                else:
                    return fecha                