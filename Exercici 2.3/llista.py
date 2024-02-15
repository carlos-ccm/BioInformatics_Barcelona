import random

def generadorAleatori(notes):
    llista = []
    for i in range(notes):
        num = random.randint(0,10)
        llista.append(num)
    return llista

def generaNotesAlumne(numero, nom):
    resultat = []
    resultat.append(nom)
    aleatoria = generadorAleatori(numero)
    resultat.append(aleatoria)
    return resultat