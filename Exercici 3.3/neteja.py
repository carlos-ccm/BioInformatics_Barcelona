import numpy as np
import pandas as pd


def neteja(file_input):
    print("Activitat de processat")
    dfRAW = pd.read_csv(file_input,delimiter=";")
    
    dfRAW['altura'] = pd.to_numeric(dfRAW['altura'], errors = 'coerce')
    dfRAW['imc'] = pd.to_numeric(dfRAW['imc'], errors = 'coerce')
    dfRAW['peso'] = pd.to_numeric(dfRAW['peso'], errors = 'coerce')
    dfRAW = dfRAW.dropna(subset=['altura','peso','imc'])

    dfGenero = dfRAW[(dfRAW['genero'] == 'Hombre') | (dfRAW['genero'] == 'Mujer')]
    
    dfValores = dfGenero[(dfGenero['altura'] > 0) & (dfGenero['peso'] > 0) &
                         (dfGenero['imc'] > 0)]
    
    dfValores_filtrado = dfValores[(dfValores['altura'] < 3) & (dfValores['peso'] < 500) &
                         (dfValores['imc'] < 50)]
    
    return dfValores_filtrado
    
if __name__ == "__main__":
    
    clean_dataframe = neteja(file_input = "raw.csv")
    print(clean_dataframe)