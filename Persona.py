"""
Definiendo la estructura de datos Persona, modelada en el diagrama UML
"""
class Persona:
    #Constructor de la clase Persona
    #El self hace referencia a la instancia actual del objeto, permite acceder a los atributos
    def __init__(self, cod, nom, ape):
        self.__codigo = cod
        #Se utiliza el doble guion bajo para definir el ambito privado
        self.nombre = nom
        #Sin guion bajo el ambito es publico
        self._apellido = ape
        #Un guion bajo define un ambito protegido
    
    #Metodo setter: permite modificar un atributo fuera del constructor
    def setCodigo(self, cod):
        self.__codigo = cod
        
    #Metodo getter: permite obtener el valor de un atributo
    def getCodigo(self):
        return self.__codigo
    
    def setNombre(self, nom):
        self.nombre = nom
        
    def getNombre(self):
        return self.nombre
    
    def setApellido(self, ape):
        self._apellido = ape
        
    def getApellido(self):
        return self._apellido
    
#Declarando la variable ob1 del tipo Persona e inicializacion (Clase)
#Instancia de la clase
ob1 = Persona(1, "Juan", "Perez")

#__codigo no se puede modificar porque es privado
ob1.__codigo = 10
ob1.nombre = "Maria"
ob1._apellido = "Alarcon"

ob2 = Persona(2, "Mario", "Diaz")

#Guardando en una lista los objetos instanciados
lst = [ob1, ob2]

#Imprimiendo en una cadena los items tipo Persona de la lista
for item in lst:
    print(str(item.getCodigo()) + " " + item.getNombre() + " " + item.getApellido())
