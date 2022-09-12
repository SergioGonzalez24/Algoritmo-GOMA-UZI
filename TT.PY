import string
import pandas as pd
import numpy as np
import glob
import os
import datetime

import time


def merger(tareas_generadas : string, tiendasyproductos : string) -> list:
    # merging the files
    files_joined = os.path.join(tareas_generadas, './*csv') #Remplazar con la ruta del directirio que contenga los archivos

    # Return a list of all joined files
    list_files = glob.glob(files_joined)

    print("* Merging multiple csv files into a single pandas dataframe *")
    # Merge files by joining all files
    df2 = pd.concat(map(pd.read_csv, list_files), ignore_index=True)

    df2["sku_cadena"] = df2["sku_cadena"].astype(str)


    df3 = pd.read_excel(tiendasyproductos, sheet_name='Tiendas') #Remplazar con la ruta del directirio que contenga los archivos
    df3.rename(columns = {'Código local B2B':'codigo_local_cadena'}, inplace = True)


    df4 = pd.read_excel(tiendasyproductos, sheet_name='Productos') #Remplazar con la ruta del directirio que contenga los archivos
    df4.rename(columns = {'Sku B2B':'sku_cadena'}, inplace = True)
    df4["sku_cadena"] = df4["sku_cadena"].astype(str)

    df2 = df2[df2['asigna_tarea'].isin([1])]
    df2 = df2[df2['producto'].isin([1])]
    df2 = df2[~df2['tareas'].isin(['presencia','presencia2'])]

    df2 = df2.drop(['foto','id_proceso', 'score_fin'], axis=1)

    c2 = pd.merge(df2, df3, on="codigo_local_cadena")
    c2 = pd.merge(c2, df4, on="sku_cadena")
    c2 = c2.drop(['fecha'], axis=1)

    c4 = c2.sort_values(['sku_cadena', 'Nombre del Local', 'tareas', 'fecha_tarea'])
    c5 = c4.drop(['fecha_tarea','asigna_tarea','producto','Cadena'], axis=1)
    c6 = c5.to_numpy().tolist()
    
    return c6

def prueba_datos(datos : list) -> list:
    
    valor_estatico = 0
    lista_analisis = []
    
    for fila in range(len(datos)):
        repetidor = 1
        cant_elementos_borrar = 0
        
        if len(datos) == 1:
                    lista_analisis.append([datos[valor_estatico],1])
                    return lista_analisis
  
            
        
        for elemento  in range(1,len(datos)):
            if datos[valor_estatico] == datos[elemento]:
                repetidor += 1
                
                if len(datos) == 2:
                    lista_analisis.append([datos[valor_estatico],2])
                    return lista_analisis
                

                
            elif datos[valor_estatico] != datos[elemento]:
                cant_elementos_borrar = repetidor                 
                lista_analisis.append([datos[valor_estatico],repetidor])
                
                
                break

        for borrado in range(cant_elementos_borrar):
                    datos.pop(valor_estatico)
    return lista_analisis
   
   
if __name__ == "__main__":
    # datos = ["hola",['a', 'b', 'c'],['a', 'b', 'c'],['a', 'b', 'c'],['1', '2', '3'],['a', 'b', 'c'],['1', '2', '3'],['1', '2', '3']]
    # datos = [['a', 'b', 'c'],['a', 'b', 'c'],['a', 'b', 'c'],['1', '2', '3'],['a', 'b', 'c'],['1', '2', '3']]
    # datos = [
    #     ["HOLA"],["HOLA"],["HOLA"],
    #     ["HOLA"],["ADIOS"],["HOLA"],
    #     ["123"],["123"],["123"],
    #     ["HOLA"],["HOLA"],["HOLA"],
    #     ["ADIOS"],["ADIOS"],["123"],
    #     [123],[123],[123],
    #     [True],[False],[True],
    #     ]
    #Lectura y consolidación de archivos de Tareas Generadas
    a = '/Users/uz/Downloads/RetoTec/Tareas_Generadas'
    b = '/Users/uz/Downloads/RetoTec/Bases_Tiendas y Productos.xlsx'

    print(prueba_datos(merger(a,b)))     
    
