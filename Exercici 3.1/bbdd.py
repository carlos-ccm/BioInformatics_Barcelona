import sqlite3

#Funció per crear la base de dades i la taula
def crear_base_de_dades(nom_bbdd):
    # Connecta amb la base de dades (si no existeix, la crearà)
    conn = sqlite3.connect(nom_bbdd)
    c = conn.cursor()
    # Crea la taula 'clients' amb les columnes especificades
    c.execute('''CREATE TABLE IF NOT EXISTS clients
        (id INTEGER PRIMARY KEY,
        nom TEXT,
        cognom TEXT,
        pes REAL,
        alcada REAL,
        edat INTEGER,
        data_matriculacio DATE)''')
    # Guarda els canvis i tanca la connexió
    conn.commit()
    conn.close()
    
def inserir_client(nom, cognom, pes, alcada, edat, data_matriculacio):
    conn = sqlite3.connect("activitat3.sqlite")
    c = conn.cursor()
    # Inserció d'una nova fila amb les dades del client
    c.execute('''INSERT INTO clients (nom, cognom, pes, alcada, edat, data_matriculacio)
    VALUES (?, ?, ?, ?, ?, ?)''', (nom, cognom, pes, alcada, edat, data_matriculacio))
    # Guarda els canvis i tanca la connexió
    conn.commit()
    conn.close()
    
def esborrar_client_per_nom_cognom(nom,cognom):
    conn = sqlite3.connect("activitat3.sqlite")
    c = conn.cursor()
    
    c.execute("DELETE FROM clients WHERE nom = ? AND cognom = ?",(nom,cognom))
    conn.commit()
    
    if c.rowcount > 0:
        print(f"Persona {nom} {cognom} esborrada amb exit")
    else:
        print("No s'ha trobat cap nom a la base de dades")
        
def obtenir_tots_els_clients():
    conn = sqlite3.connect('base_de_dades.db')
    c = conn.cursor()
    # Executa una consulta SELECT per obtenir tots els clients
    c.execute("SELECT * FROM clients")
    clients = c.fetchall()
    # Imprimeix els clients
    for client in clients:
        print(client)
    # Tanca la connexió
    conn.close()

def seleccionar_clients_per_nom(nom):
    conn = sqlite3.connect('base_de_dades.db')
    c = conn.cursor()
    # Consulta SQL per seleccionar les entrades amb el nom proporcionat
    c.execute("SELECT * FROM clients WHERE nom = ?", (nom,))
    resultats = c.fetchall()
    # Mostra els resultats
    if len(resultats) > 0:
        print("Resultats per al nom:", nom)
    for resultat in resultats:
        print(resultat)
    else:
        print("No s'han trobat resultats per al nom:", nom)
    # Tanca la connexió
    conn.close()

def ordenar_clients_per_edat():
    conn = sqlite3.connect('base_de_dades.db')
    c = conn.cursor()
    # Consulta SQL per seleccionar totes les entrades ordenades per edat
    c.execute("SELECT * FROM clients ORDER BY edat")
    resultats = c.fetchall()
    # Mostra els resultats ordenats per edat
    print("Clients ordenats per edat:")
    for resultat in resultats:
        print(resultat)
    # Tanca la connexió
    conn.close()

def esborrar_client_per_id(id):
    conn = sqlite3.connect('base_de_dades.db')
    c = conn.cursor()
    # Consulta SQL per esborrar una entrada amb l'ID proporcionat
    c.execute("DELETE FROM clients WHERE id = ?", (id,))
    conn.commit()
    # Verifica si s'ha esborrat correctament
    if c.rowcount > 0:
        print(f"Entrada amb ID {id} esborrada amb èxit.")
    else:
        print(f"No s'ha trobat cap entrada amb ID {id}.")
    # Tanca la connexió
    conn.close()

def esborrar_taula_clients():
    conn = sqlite3.connect('activitat3.sqlite')
    c = conn.cursor()
    # Consulta SQL per esborrar la taula clients
    c.execute("DROP TABLE IF EXISTS clients")
    conn.commit()
    12
    print("Taula 'clients' esborrada amb èxit.")
    # Tanca la connexió
    conn.close()
    
def actualitzar_pes_client_per_id(id_client, nou_pes):
    conn = sqlite3.connect('base_de_dades.db')
    c = conn.cursor()
    # Consulta SQL per actualitzar el pes del client amb l'ID proporcionat
    c.execute("UPDATE clients SET pes = ? WHERE id = ?", (nou_pes, id_client))
    conn.commit()
    # Verifica si s'ha actualitzat correctament
    if c.rowcount > 0:
        print(f"Pes del client amb ID {id_client} actualitzat amb èxit.")
    else:
        print(f"No s'ha trobat cap client amb ID {id_client}.")
    # Tanca la connexio
    conn.close()