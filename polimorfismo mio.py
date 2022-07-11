class Concesionario():
    def __init__(self,disponibles=10,ventas=0):
        self.disponibles=disponibles
        self.ventas=ventas

    def storno(self):
        self.disponibles = self.disponibles - 1
        print("El número de coches disponibles es: ",self.disponibles)

class Coche():
    def __init__(self,color,modelo):
        self.color=color
        self.modelo=modelo

    def datoscoche(self):
        print(self.color,self.modelo)    

while True:

    print("Elige un modelo: ")
    print("1. BMW")
    print("2. Audi")
    print("3. Ferrari")
    print("4. Fiat")

    eleccionmodelo=input(">")

    print("Elige un color: ")
    print("1. Rojo")
    print("2. Blanco")
    print("3. Azul")
    print("4. Amarillo")

    eleccioncolor=input(">")

    macchina= Coche(eleccioncolor,eleccionmodelo)
    contar=Concesionario()

    if eleccioncolor !=False and eleccionmodelo !=False:
        Coche.datoscoche()
        contar.storno()
    elif eleccionmodelo==0:
        break    

