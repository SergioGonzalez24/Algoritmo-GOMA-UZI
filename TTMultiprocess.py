from multiprocessing import Process

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
   
  
def main() -> None:
    
    datos = [
        ["HOLA"],["HOLA"],["HOLA"],
        ["HOLA"],["ADIOS"],["HOLA"],
        ["123"],["123"],["123"],
        ["HOLA"],["HOLA"],["HOLA"],
        ["ADIOS"],["ADIOS"],["123"],
        [123],[123],[123],
        [True],[False],[True],
        ]
    
    
  
        
if __name__ == "__main__":
    # datos = ["hola",['a', 'b', 'c'],['a', 'b', 'c'],['a', 'b', 'c'],['1', '2', '3'],['a', 'b', 'c'],['1', '2', '3'],['1', '2', '3']]
    # datos = [['a', 'b', 'c'],['a', 'b', 'c'],['a', 'b', 'c'],['1', '2', '3'],['a', 'b', 'c'],['1', '2', '3']]
    
    
    #  print(prueba_datos(datos))     
    
    
    main()
