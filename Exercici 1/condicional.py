#OBLIGATORIS

#Exercici 1
'''
Comprovació de nombre positiu o negatiu:
Demana a l'usuari que introdueixi un nombre i mostra si és positiu, negatiu o zero.
'''

#Li demanem a l'usuari que introdueixi un numero
numero = int(input("Introdueix un numero: "))

if numero > 0:
    print("Nombre positiu")
elif numero < 0:
    print("Nombre negatiu")
else:
    print("El nombre es zero")
  
#Exercici 2
'''
Determinar si un nombre és divisible per 3 i/o 5:
Sol·licita a l'usuari que introdueixi un nombre i comprova si és divisible per 3 i/o 5.
'''
#Li demanem a l'usuari que introdueixi un numero
numero = int(input("Introdueix un numero: "))

if (numero % 3) == 0:
    print("Divisible entre 3")
if (numero % 5) == 0:
    print("Divisible entre 5")
else:
    print("No es divisible entre 3 ni 5")

#Exercici 3
'''
Determinar l'any de traspàs:
L'usuari introdueix un any. Verifica si és un any de traspàs o no.
'''
#Li demanem a l'usuari que introdueixi un any
any = int(input("Introdueix un any per saber si es de traspas o no: "))

if any >= 0:
    if (any % 4) == 0:
        if (any % 100) == 0 and (any % 400) == 0:
            print("Any de traspas")
        elif (any % 100) == 0 and (any % 400) != 0:
            print("No es any de traspas")
        else:
            print("Any de traspas")
    else:
        print("No es any de traspas")
else:
    print("No hi ha anys negatius")

#Exercici 4
'''   
Conversió de notes a qualificacions:
L'usuari introdueix una puntuació (de 0 a 100). Converteix aquesta puntuació en una
qualificació (A, B, C, D, F) amb les següents franges:
''' 
#Li demanem a l'usuari que introdueixi una nota
nota = int(input("Introdueix una nota: "))

if 100 >= nota >= 90:
    nota = "A"   
elif 89 >= nota >= 80:
    nota = "B"  
elif 79 >= nota >= 70:
    nota = "C"
elif 69 >= nota >= 60:
    nota = "D"
else:
    nota = "F"
    
print(f"La teva nota es: {nota}")

#Exercici 5
'''   
Comparació de cadenes:
Sol·licita dues cadenes de text de l'usuari i determina si són iguals o diferents.
''' 

cadena_1 = input("Introdueix una primera cadena: ")
cadena_2 = input("Introdueix una segona cadena: ")

if cadena_1 == cadena_2:
    print("Son iguals")
else:
    print("Son diferents")
######################################################################################

#OPCIONALS

#Exercici 1
'''
Conversió d'hores a format de 12 hores:
L'usuari introdueix una hora en format de 24 hores. Converteix-la a format de 12 hores i
afegeix "AM" o "PM".
'''

#Introdueix la hora en format 24h
hora = int(input("Introdueix una hora en format 24h: "))

if 0 <= hora <= 24:
    if hora > 12:
        print("Son les",hora - 12,"PM")
    else:
        print("Son les",hora,"AM")
else:
    print("Hora incorrecta") 
    
#Exercici 2
'''
Calculadora de taxes d'impostos:
Crea una calculadora d'impostos que demani a l'usuari que introdueixi el seu sou i determini
la taxa d'impostos segons les següents franges:
'''
#Introdueix el sou
sou = float(input("Introdueix el teu sou: "))

if sou > 50000:
    print("Els impostos a pagar son:",sou * 0.2)
elif sou > 10000:
    print("Els impostos a pagar son:",sou * 0.1)
else:
    print("Els impostos a pagar son:",sou * 0.05)
