from pickle import FALSE


dato=input("Introduce un valor no falso" )
print(len(dato), type(dato))
print(bool(dato))
if (bool(dato) != False):
    print ("El valor es" + dato)
else:
    print("El valor es falso")

lista1=input("Introduce un valor", )
lista2=input("Introduce otro valor", )
lista3=input("Introduce el último valor")
if((bool(lista1) != False and bool(lista2) != False and bool(lista3) !=False)):
    lista=[lista1,lista2,lista3]
    print(lista)
else:
    print('El valor es falso')
numero1=input("Introduce un número entero", )
numero2=input("Introduce otro número entero", )
numero3=input("Introduce el último número entero", )
if (bool(numero1) !=False and bool(numero2) !=False and bool(numero3) !=False):
    numeros=[numero1,numero2,numero3]
    print(numeros)
else:
    print("Uno de los números es un false")    