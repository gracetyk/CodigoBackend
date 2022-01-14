class Persona:
    #variables > atributos
    nombre=''
    edad=0
    estatura=0.0
    #funcion > metodo
    def saludar():
        print('Hola!')
    #constructor es el encargado de inicializar los atributos de la clase
    #siempre en todo metodo como parametro debe ir el self(sirve para refereiar a lla 
    # copia que estamos usando)
    def __init__(self,nombre_de_la_persona,edad_persona,estatura_persona) :

        self.nombre=nombre_de_la_persona
        self.edad=edad_persona
        self.estatura=estatura_persona
        self.sexo='NS/NO'
 #cuando una variable le asignamsuna clase , pasa a llamr una instancia de la clase (
 # #copia de la clase con todos sus atributos y metodos)
eduardo=Persona(nombre_de_la_persona='Eduardo',edad_persona=20,estatura_persona=1.89)
print(eduardo.nombre)
print(eduardo.sexo)
eduardo.saludar()

