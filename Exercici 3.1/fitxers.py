import csv

def mostrar_fitxer_python(nom_fitxer):
    try:
        with open(nom_fitxer, "r") as fitxer:
            contingut = fitxer.read()
            print("Contingut del fitxer", nom_fitxer, ":\n")
            print(contingut)
    except FileNotFoundError:
        print("El fitxer", nom_fitxer, "no existeix.")

def mostrar_linies_fitxer(nom_fitxer):
    try:
        with open(nom_fitxer, "r") as fitxer:
            print("Contingut del fitxer", nom_fitxer, "línia per línia:\n")
            for linia in fitxer:
                print(linia, end="") # Mostrem la linia sense salt de línia
    except FileNotFoundError:
        print("El fitxer", nom_fitxer, "no existeix.")
        
def copiar_fitxer(origen, desti):
    try:
        with open(origen, "r") as fitxer_origen:
            with open(desti, "w") as fitxer_desti:
                contingut = fitxer_origen.read()
                fitxer_desti.write(contingut)
                print("S'ha copiat el contingut de", origen, "a", desti)
    except FileNotFoundError:
        print("El fitxer origen no existeix.")
    except Exception as e:
        print("S'ha produït un error:", str(e))

def llegeixCSV (fitxer):
    llista = []
    # Abre el archivo en modo de lectura ('r') y especifica el delimitador si es necesario
    with open(fitxer, 'r', newline='') as archivo:
        # Crea un lector CSV
        lector_csv = csv.reader(archivo)
    # Itera sobre las filas del archivo CSV
        for fila in lector_csv:
    # Cada fila es una lista de valores separados por comas
            print(fila)
            llista.append(fila)
            
    return(llista)

def crearCSV(llista,fitxer):
    # Ruta del archivo CSV donde deseas escribir
    
    # Abre el archivo en modo de escritura ('w') y especifica el delimitador si es necesario
    with open(fitxer, 'w', newline='') as archivo:
        # Crea un escritor CSV
        escritor_csv = csv.writer(archivo)
        # Escribe los datos en el archivo CSV
        for fila in llista:
            escritor_csv.writerow(fila)
            
def head(nom_fitxer,num):
    try:
       with open(nom_fitxer,"r") as fitxer:
           for i,linia in enumerate(fitxer):
               if i < num:
                    print(linia,end = "")
               else:
                   break
    except FileNotFoundError:
        print("El fitxer", nom_fitxer, "no existeix.")
    
def numlinies(nom_fitxer):
    try:
       with open(nom_fitxer,"r") as fitxer:
        for i,linia in enumerate(fitxer):
            pass   
        print(f"El fitxer {nom_fitxer} te {i+1} linies")
    except FileNotFoundError:
        print("El fitxer", nom_fitxer, "no existeix.")

def tail(nom_fitxer,num):
    try:
       with open(nom_fitxer,"r") as fitxer:
            linies = fitxer.readlines()[-num:]
            for i in linies:
                print(i)
    except FileNotFoundError:
        print("El fitxer", nom_fitxer, "no existeix.")
