import random

class Val():

    def generarClave():
        pat = chr(random.randint(65, 90))
        pat = pat + chr(random.randint(65, 90))
        pat = pat + chr(random.randint(35, 38))
        pat = pat + chr(random.randint(97, 122))
        pat = pat + chr(random.randint(97, 122))
        pat = pat + chr(random.randint(97, 122))
        pat = pat + chr(random.randint(35, 38))
        pat = pat + str(random.randint(0, 9))
        pat = pat + str(random.randint(0, 9))
        pat = pat + str(random.randint(0, 9))
        return pat
        
    def validarSexo():
        sexo = None
        while sexo == None:
            sexo = input("--Indique el sexo (M-F): ")
            if sexo == "M" or sexo == "F":
                return sexo
            else:
                sexo = None

    def validarRol():
        rol = None
        while rol == None:
            rol = input("--Indique el rol (JR-RH-TJ): ")
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

    def validarInt(pregunta):
        numero = None
        while numero == None:
            numero = input(pregunta)
            if numero == "" or numero == None:
                numero = None
            else:
                return numero

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
                print ("¡Largo de fecha no valido!")
                fecha = None
            else:
                if fecha[4] != "-" and fecha[7] != "-":
                    print ("¡Formato de fecha no valido!")
                    fecha = None
                else:
                    fechaSeparada = fecha.split("-")
                    if fechaSeparada[0].isnumeric() and fechaSeparada[1].isnumeric() and fechaSeparada[2].isnumeric():
                        if int(fechaSeparada[0]) < 1000:
                            print("!Año no valido!")
                            fecha = None
                        else:
                            if int(fechaSeparada[1]) >= 1 and int(fechaSeparada[1]) <= 12:
                                if int(fechaSeparada[2]) >= 1 and int(fechaSeparada[2]) <= 31:
                                    if (int(fechaSeparada[1]) == 4 or int(fechaSeparada[1]) == 6 or int(fechaSeparada[1]) == 9 or int(fechaSeparada[1]) == 11 ) and (int(fechaSeparada[2]) == 31):
                                        print("¡Dia no valido!")
                                        fecha = None
                                    else:
                                        if int(fechaSeparada[1]) == 2 and int(fechaSeparada[2]) == 30:
                                            print("¡Dia no valido!")
                                            fecha = None
                                        else:
                                            return fecha
                                else:
                                    print("¡Dia no valido!")
                                    fecha = None
                            else:
                                print("¡Mes no valido!")
                                fecha = None              
                    else:
                        print ("¡Solo se permiten caracteres numericos!")
                        fecha = None

print(Val.generarClave())