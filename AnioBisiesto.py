"""
Clase Fecha para determinar si un año es bisiesto o no
"""
class Fecha:
    #Metodo constructor
    def __init__(self, dia, mes, anio):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio

    #Metodo para modificar nuevamente los atributos
    def setFecha(self, dia, mes, anio):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio

    #Metodo para retornar la fecha con su formato
    def getFecha(self):
        return str(self.__dia) + "/" + str(self.__mes) + "/" + str(self.__anio)

    #Logica para definir si el año es bisiesto o no, devuelve bool
    def esValida(self):
        valida = False
        if self.__anio > 0:
            if self.__mes == 4 or self.__mes == 6 or self.__mes == 9 or self.__mes == 11:
                if self.__dia > 0 and self.__dia <=30:
                    valida = True
            else:
                if self.__mes ==2:
                    if ((self.__anio%4==0 and self.__anio%100!=0) or (self.__anio%4==0 and self.__anio%400==0)):
                        if self.__dia > 0 and self.__dia <=29:
                            valida = True
                    else:
                        if self.__dia > 0 and self.__dia <=28:
                            valida = True
                else:
                    if self.__mes>0 and self.__mes <=12:
                        if self.__dia > 0 and self.__dia <=31:
                            valida = True
        return valida

#Instnaciando la clase Fecha
f1 = Fecha(31,12,2022)

#If para imprimir si la fecha es valida o no
if f1.esValida():
    print(f"La fecha {f1.getFecha()} es valida")
else:
    print(f"La fecha {f1.getFecha()} NO es valida")