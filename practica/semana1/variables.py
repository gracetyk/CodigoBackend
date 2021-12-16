nombre=input("Ingrese su nombre")
edad=input("Ingrese su edad")
ecivil=input("Estado civil")

if ecivil=="C":
    valorec="CASADO"

elif ecivil=="V":
    valorec="viudo"
else:
    valorec="SOLTERO"

print("Hola",nombre, "Su estado civil:",valorec)