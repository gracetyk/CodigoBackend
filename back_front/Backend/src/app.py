from flask import Flask,request
from flask_cors import CORS

app= Flask(__name__)

CORS(app=app)

usuarios =[{
    "nombre":"Enrique",
    "apellido":"Obregozo",
    "area":"contabilidad",
    "fecha_inicio":"2021-03-12",
    "dni":"41007942"
},
{
    "nombre":"Juan",
    "apellido":"Perez",
    "area":"contabilidad",
    "fecha_inicio":"2021-03-12",
    "dni":"41007942"
}]

@app.route('/users', methods=['POST'])
def createUser():
    print (request.json)
    return 'received'

@app.route('/users', methods=['GET'])
def getUsers():
    return 'received'

@app.route('/user/<id>', methods=['GET'])
def getUser():
    return 'received'

@app.route('/users/<id>', methods=['GET'])
def deleteUser():
    return 'received'

@app.route('/users/<id>', methods=['PUT'])
def updateUser():
    return 'received'

if __name__ == "__main__":
    app.run(debug=True)