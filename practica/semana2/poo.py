class cursos:
    def __init__(self,nombre,precio,dura):
        self.nombre=nombre
        self.precio=precio
        self.dura=dura

    def imprimirdetalle(self):
        print(self.nombre,self.precio,self.dura)

    def mensajecosto(self):

        if self.precio>500:
            print("El curso es caro")
        else:
            print("el curso es accesible")



curso1=cursos("python",200,"5 mes")
curso1.imprimirdetalle()
