#Exercici 1
'''
Verificació d'edad:
Demana al usuari que introdueixi un numero. Per continuar el número ha de ser major o
igual a 18
'''

edat = int(input("Introdueix la teva edat: "))

while edat < 18:
    print("Edat no valida")
    edat = int(input("Introdueix la teva edat: "))

#Exercici 2
'''
Verificació de Contrasenya:
Demana a l'usuari que introdueixi una contrasenya. Utilitza un bucle while per assegurar-te
que la contrasenya té almenys 8 caràcters. Fes servir la funció len() per mirar el tamany de
la contrasenya
'''
cond = True
while cond:
    password = input("Introdueix una contrasenya: ")
    if len(password) >= 8:
        cond = False
        print("Contrasenya correcta")
        
#Exercici 3
'''
Lector de lletres
Fes un programa que llegeixi lletra a lletra el contingut d'un string. Llegeix també de final a
començament
'''
#Demanem que l'usuari introdueixi un string
contingut = input("Introdueix un string: ")
print("En ordre:")
for i in range(len(contingut)):
    print(contingut[i])
print("De final a començament:")
for i in range(len(contingut)-1,-1,-1):
    print(contingut[i])