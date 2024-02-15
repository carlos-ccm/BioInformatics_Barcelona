'''
Fes un programa que llegeix un texte per teclat. El programa haura de
    - Contar quants caràcters hi ha
    - Convertir els caracter en majuscula
    - Contar cuantes paraules hi ha
    - Separar la cadena en frases (separador el punt)
'''

text = input("Introdueix un text per a que sigui processat:")
#Quants caracters hi ha
print(len(text))

#En majuscula
print(text.upper())

#Contar paraules
print(len(text.split(" ")))

#Separar en frases
print(text.split("."))

