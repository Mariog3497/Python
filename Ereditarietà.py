class Mario():
    datospersonales=[]
    nombre="nombre"
    apellido="apellido"
    edad=15
    trabajo="trabajo"

    

Persona=Mario()

Persona.nombre=input("Introduce tu nombre: ")
if type(Persona.nombre==str):
    Persona.datospersonales.append(Persona.nombre)

Persona.apellido=input("Introduce tu apellido: ")
if type(Persona.apellido==str):
    Persona.datospersonales.append(Persona.apellido)

Persona.edad=input("Introduce tu edad: ")
if type(Persona.edad==int):
    Persona.datospersonales.append(Persona.edad)

Persona.trabajo=input("Introduce el trabajo: ")
if type(Persona.trabajo==str):
    Persona.datospersonales.append(Persona.trabajo)

print(Persona.datospersonales)
else:
    print("Algún dato es incorrecto")