from ast import Return


class Val():

    def validarSexo():
        sexo = None
        while sexo == None:
            sexo = input("Indique el sexo (M-F): ")
            if sexo == "M" or sexo == "F":
                return sexo
            else:
                sexo = None
        
