"""
Multiplicacion Rusa con programación orientada a objetos
"""
class Rusa:
    def __init__(self, num1, num2):
        self.__multiplicando = num1
        self.__multiplicador = num2
        self.__calcular()

    #Definiendo el método calcular como privado
    def __calcular(self):
        self.__resultado = 0
        n1 = self.__multiplicando
        n2 = self.__multiplicador
        while n1 > 0:
            if n1%2!=0:
                self.__resultado += n2
            n1 = n1//2
            n2 = n2*2

    def setDatos(self, num1, num2):
        self.__multiplicando = num1
        self.__multiplicador = num2
        self.__calcular()

    def getMultiplicando(self):
        return self.__multiplicando

    def getMultiplicador(self):
        return self.__multiplicador

    def getResultado(self):
        return self.__resultado

#Instanciando la clase Rusa desde su metodo constructor
op1 = Rusa(5,2)
print(f"El resultado para {op1.getMultiplicando()} y {op1.getMultiplicador()}")
print(op1.getResultado())

#Instanciando desde el metodo setDatos para modificar el multiplicando y multiplicador
op1.setDatos(4,5)
print(f"El resultado para {op1.getMultiplicando()} y {op1.getMultiplicador()}")
print(op1.getResultado())
