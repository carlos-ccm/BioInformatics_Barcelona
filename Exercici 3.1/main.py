import bbdd
import fitxers

def main():
    print("Hola! Aquest es el meu programa d'activitat 3.\n")
    '''
    fitxers.mostrar_fitxer_python("ejemplo.txt")
    fitxers.copiar_fitxer("ejemplo.txt","nuevo_archivo.txt")
    fitxers.llegeix_csv("clients.csv")
    
    bbdd.crear_base_de_dades("activitat3.sqlite")
    bbdd.inserir_client('Anna', 'Garcia', 65.5, 1.68, 30, '2024-02-18')
    bbdd.inserir_client('David', 'Lopez', 75.2, 1.75, 35, '2024-02-19')
    bbdd.inserir_client('Laura', 'Martinez', 55.0, 1.60, 25, '2024-02-20')
    '''
    fitxers.head("ejemplo.txt",1)
    fitxers.numlinies("ejemplo.txt")
    fitxers.tail("ejemplo.txt",5)
    llista = fitxers.llegeixCSV("clients.csv")
    print(llista)
    fitxers.crearCSV(llista,"new_clients.csv")
    
if __name__ == "__main__":
    main()
