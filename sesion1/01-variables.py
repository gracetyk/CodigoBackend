numero=10
numero2=10.5
numero ="Febrero"
nombre= "Eduardo"
fecha=0

#variable de texto o string
nombre="Eduardo"
apellido='Ramiro'

fecha =0

html=''' <html>
<p>
</p>'''
print('holaaa :)')
print (type(nombre))
#str=string
print (type(numero))
#bool=boolean
soltero=True

print (type(soltero))

#variables que tienen varios valores
#arreglos listas
edades = [10,12,40,60,'Eduardo',14.5,False,[1,2]]
#para ingresar a los valores de una lista 
print(edades[-5:-1])
print(edades[:])
print(edades[1:-1])
print(edades[1:3])




#json (javascript object Notation | Diccionario)

curso={
    'nombre': 'Backend',
    'nombre': 'frontend',
    'dificultad': 'Dificil',
    'skills':[
        {
            'nombre':'Base de datos',
            'nivel':'Intermedio'
        },
        {
            'nombre':'ORM',
            'nivel':'Avanzado'
        }
    ]
}

print (curso['dificultad'])
print (curso['skills'][1]['nombre'])



personas = [{
    'nombre': 'Eduardo',
    'nacionalidad': 'peruano',
    'hobbies':[
        {
            'nombre': 'Volar drones',
            'experiencia': '2 años'
        },{
            'nombre':'Programar',
            'experiencia': '1 mes'
        }
    ]
},{
    'nombre': 'Juliana',
    'nacionalidad': 'colombiana',
    'hobbies':[
        {
            'nombre': 'Montar bici',
            'experiencia': '4 años'
        },{
            'nombre':'Bases de datos',
            'experiencia': '8 mes'
        }
    ]
}]

print(personas[0]['nacionalidad'])
print(personas[1]['hobbies'][0]['nombre'])
print(personas[1]['hobbies'])
print(personas[0]['hobbies'][1]['experiencia'])

