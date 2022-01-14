from flask import Flask 
#En python tenemos varais variables que son de uso propio de python no podemos modificar ni alterar
#__main__ >esta variable sirve para idicar si estamos en el archivo principal del proyecto

app= Flask(__name__)

#el decorado sirve parael metodo de una clse pero implementandolo en una fucnion

@app.route('/')
def inicio():
    return 'Bienvendo a m API'

@app.route('/bienvenido')
def bienvenida():
    return 'Te doy la bienv'

@app.route('/bienvenido/home')
def bienvenido_home():
    return '1'

if __name__=='__main__':
    app.run(debug=True,port=3000)

