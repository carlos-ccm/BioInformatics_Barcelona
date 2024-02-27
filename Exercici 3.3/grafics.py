import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import neteja



def main(file_input):
    df = neteja.neteja(file_input = file_input)
    print(df)
    # Separar los datos según el sexo
    df_hombres = df[df['genero'] == 'Hombre']
    df_mujeres = df[df['genero'] == 'Mujer']
    # Crear el gráfico de dispersión
    plt.figure(figsize=(8, 6))
    plt.scatter(df_hombres['altura'], df_hombres['peso'], color='blue', label='Hombre')
    plt.scatter(df_mujeres['altura'], df_mujeres['peso'], color='pink', label='Mujer')
    # Añadir etiquetas y título
    plt.title('Gráfico de Dispersión de Altura vs Peso')
    plt.xlabel('Altura (cm)')
    plt.ylabel('Peso (kg)')
    plt.legend()
    plt.show()

    
if __name__ == "__main__":
    file_input = "raw.csv"
    main(file_input=file_input)