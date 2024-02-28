import numpy as np
import pandas as pd

array_1d = np.array([1, 2, 3, 4, 5])
print("Array de 1 dimensió:")
print(array_1d)
print(array_1d[0])

matriu_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Array de 2 dimensions (matriu):")
print(matriu_2d)
print(matriu_2d[0,0])
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

# Crear un array de 3 dimensions (tensor)
tensor_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print("Array de 3 dimensions (tensor):")
print(tensor_3d)
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

arr = np.array([1, 2, 3, 4, 5])
x = arr
arr[0] = 42

print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

# Crear un array de 1000 valors aleatoris entre 0 i 1
array_aleatori = np.random.normal(3,4,1000000)

import matplotlib.pyplot as plt

# Visualitzar l'array com a histograma
plt.hist(array_aleatori, bins=30, color='skyblue', edgecolor='black')
plt.title("Histograma de 1000 valors aleatoris entre 0 i 1")
plt.xlabel("Valor")
plt.ylabel("Freqüència")
plt.grid(True)
plt.show()


x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1, arr2)

print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr1, arr2)

print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr1, arr2)

print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr1, arr2)

print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.mod(arr1, arr2)

print(newarr)

arr = np.around(3.1666, 2)

print(arr)

array_hombre = np.full(10, "hombre")
print(array_hombre)

matriz_a = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])

matriz_b = np.array([[9, 8, 7],
                        [6, 5, 4],
                        [3, 2, 1]])

# Multiplicar las matrices
resultado = np.dot(matriz_a, matriz_b)

print("Matriz A:")
print(matriz_a)
print("\nMatriz B:")
print(matriz_b)
print("\nResultado de la multiplicación de las matrices:")
print(resultado)


#####################################################################################
# Crear una sèrie amb una llista de nombres
serie_nombres = pd.Series([10, 20, 30, 40, 50])

# Mostrar la sèrie
print("Sèrie de nombres:")
print(serie_nombres)
print()

# Accedir als valors de la sèrie
print("Primer valor de la sèrie:", serie_nombres[0])
print("Últim valor de la sèrie:", serie_nombres[4])
print()

# Accedir als valors utilitzant etiquetes d'índex personalitzades
serie_nombres.index = ['a', 'b', 'c', 'd', 'e']
print("Sèrie de nombres amb índex personalitzat:")
print(serie_nombres)
print("Valor associat a l'etiqueta 'c':", serie_nombres['c'])
print()

# Operacions aritmètiques amb sèries
serie_doble = serie_nombres * 2
print("Sèrie de nombres duplicats:")
print(serie_doble)
print()

# Filtrar valors
serie_filtrada = serie_nombres[serie_nombres > 25]
print("Sèrie de nombres filtrada (valors majors que 25):")
print(serie_filtrada)

# Crear un DataFrame amb un diccionari de dades
data = {'Nom': ['Anna', 'Pau', 'Maria', 'Joan'],
        'Edat': [25, 30, 35, 40],
        'Ciutat': ['Barcelona', 'Madrid', 'València', 'Sevilla']}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print("DataFrame:")
print(df)
print()

# Establir una nova columna com a índex
df.set_index('Nom', inplace=True)

# Mostrar el DataFrame amb l'índex canviat
print("DataFrame amb l'índex canviat:")
print(df)
print()

# Accedir a les dades utilitzant el mètode .loc[]
print("Accedir a les dades utilitzant .loc[]:")
print("Dades de l'Anna:")
print(df.loc['Anna'])
print()

# Accedir a dades específiques amb .loc[]
print("Accedir a dades específiques amb .loc[]:")
print("Edat de la Maria:", df.loc['Maria', 'Edat'])

# Crear un DataFrame amb un diccionari de dades
data = {'Nom': ['Anna', 'Pau', 'Maria', 'Joan'],
        'Edat': [25, 30, 35, 40],
        'Ciutat': ['Barcelona', 'Madrid', 'València', 'Sevilla']}

df = pd.DataFrame(data)

# Afegir una nova fila al DataFrame
nou_element = {'Nom': 'Carla', 'Edat': 28, 'Ciutat': 'Girona'}
df = df.append(nou_element, ignore_index=True)

# Mostrar el DataFrame amb el nou element afegit
print("DataFrame amb el nou element afegit:")
print(df)


# Llegir el fitxer CSV
df = pd.read_csv('nom_del_fitxer.csv')

# Verificar el nombre de files i columnes
num_files, num_columnes = df.shape

# Mostrar el nombre de files i columnes
print("Nombre de files:", num_files)
print("Nombre de columnes:", num_columnes)
