#Exercici classes
'''
Crea una classe Llibre amb els següents atributs:

titol: el títol del llibre.
autor: l'autor del llibre.
any_publicacio: l'any de publicació del llibre.
disponible: un indicador de disponibilitat del llibre (True si està disponible, False si està
prestat).
Implementa un mètode prestar() a la classe Llibre que permeti canviar l'estat de
disponibilitat del llibre a False quan és prestat.
'''
import random
import sys

class Llibre:
    def __init__(self,titol,autor,any_publicacio,disponibilitat):
        self.titol = titol
        self.autor = autor
        self.any_publicacio = any_publicacio
        self.disponibilitat = disponibilitat
    
    def prestar(self): 
        self.disponibilitat = False
    def retornar(self):
        self.disponibilitat = True
        
class LlibreFisic(Llibre):
    def __init__(self, titol, autor, any_publicacio, disponibilitat,ubicacio):
        super().__init__(titol, autor, any_publicacio, disponibilitat)
        self.ubicacio = ubicacio
    def prestar(self,nom_demandant):
        self.nom_demandant = nom_demandant
        print(f"El llibre el te: {self.nom_demandant}")
        
    def retornar(self,data_retorn):
        self.data_retorn = data_retorn
        print(f"El demandant {self.nom_demandant} ha tornat el llibre en data {self.data_retorn}")

class LlibreDigital(Llibre):
    def __init__(self, titol, autor, any_publicacio, disponibilitat):
        super().__init__(titol, autor, any_publicacio, disponibilitat)   
    def descargar(self):
        print(f"El llibre {self.titol} s'està descarregant. Tamany del fitxer {random.randint(0,100)}MB")
        print("Iniciant descarrega ...")
        for iteration in range(100000): #esto viene de la mano de chatgpt
            progress = ((iteration+1) / 100000)
            arrow = '|' * int(progress * 50)
            spaces = ' ' * (50 - len(arrow))
            sys.stdout.write('\rProgress: [{0}{1}] {2:.2f}%'.format(arrow, spaces, progress * 100))
            sys.stdout.flush()
            
llibre1 = (Llibre("Homo Deus","Yuval Noah Harari",2015,True))

Llibre.prestar(llibre1)
print(llibre1.disponibilitat)
Llibre.retornar(llibre1)
print(llibre1.disponibilitat)


llibre2 = (LlibreFisic("Homo Deus","Yuval Noah Harari",2015,True,"Badalona"))
print(llibre2.ubicacio)
llibre2.prestar("Carlos")
llibre2.retornar("14-02-2024")

llibre3 = (LlibreDigital("Homo Deus","Yuval Noah Harari",2015,True))
llibre3.descargar()