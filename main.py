import math
import random
import matplotlib.pyplot as plot
import pandas as pd


def generate_data(n: int) -> list:
    datos =[]
    
    # Calculo de particiones con formula propuesta
    
    # Creacion de n numeros aleatorios para el analisis
    for i in range(n):
        aleatorio=random.randint(10,70)
        datos.append(aleatorio)
    
    return datos


def create_table(datos, numero_particiones, intervalo, amplitud, n) -> dict:
    dicc={"Intervalo|":[],"Marca_De_Clase|":[],"Frecuencia_Absoluta|":[],"Frecuencia_Absoluta_Acomulada|":[],"Frecuencia_Relativa|":[],"Frecuencia_Relativa_Acomulada|":[]}
    frecuencia_acomulada=0
    frecuencia_relativa=0
    frecuencia_relativa_acomulada=0
    # Recorrido del for hasta n particiones
    for i in range(numero_particiones):
        frecuencia_absoluta=0    
        intervalo=intervalo+amplitud
        marca=((intervalo-amplitud)+intervalo)/2
        # recorrer la lista y mirar si esta dentro del intervalo y obtener la frecuencia absoluta
        if(i==numero_particiones-1):
            for j in datos:
                if (j>=(intervalo-amplitud) and j<=intervalo):
                    frecuencia_absoluta+=1        
        else:
            for j in datos:
                if (j>=(intervalo-amplitud) and j<intervalo):
                    frecuencia_absoluta+=1
        
        frecuencia_acomulada+=frecuencia_absoluta
        frecuencia_relativa=frecuencia_absoluta/n
        frecuencia_relativa_acomulada+=frecuencia_relativa
        # Asignacion de valores a las claves del diccionario
        dicc["Intervalo|"].append(str(intervalo-amplitud)+" - "+str(intervalo)+"|")
        dicc["Marca_De_Clase|"].append(str(marca)+"|")
        dicc["Frecuencia_Absoluta|"].append(str(frecuencia_absoluta)+"|")
        dicc["Frecuencia_Absoluta_Acomulada|"].append(str("{:.1f}".format(frecuencia_acomulada))+" - "+str("{:.1f}".format(frecuencia_relativa*100))+"%|")
        dicc["Frecuencia_Relativa|"].append(str(frecuencia_relativa)+"|")
        dicc["Frecuencia_Relativa_Acomulada|"].append(str("{:.1f}".format(frecuencia_relativa_acomulada))+" - "+str("{:.1f}".format(frecuencia_relativa_acomulada*100))+"%|")

    return dicc


def generate_plot(datos: dict):
    histograma  = pd.Series(datos) # cargamos los datos en un objeto Series
    intervalos = range(min(datos), max(datos) + 2)  # calculamos los extremos de los intervalos

    histograma.plot.hist(bins=8, color='#F2AB6D', rwidth=0.85) # generamos el histograma a partir de los datos
    plot.xticks(intervalos)
    plot.ylabel('Frecuencia')
    plot.xlabel('Edades')
    plot.title('Histograma')
    plot.savefig('plot.png')


def calcular_datos_estadisticos(data: list):
    df = pd.DataFrame({'datos': data})

    print(df['datos'].mean())
    print(df['datos'].mode().values[0])
    print(df['datos'].quantile(0.25))
    print(df['datos'].quantile(0.50))
    print(df['datos'].quantile(0.75))
    print(df['datos'].quantile(.63))

from fastapi import FastAPI
from fastapi.responses import FileResponse

# def index_main():
#     n=10
#     datos = generate_data(n)
    
#     numero_particiones=int(1+3.32*math.log10(n))
#     rango = max(datos)-min(datos)
#     amplitud=rango/numero_particiones
#     intervalo=min(datos)

#     data = create_table(datos, numero_particiones, intervalo, amplitud, n)
#     generate_plot(datos)
#     calculate_table(datos)


# app = FastAPI()

# @app.get('/')
# async def index():
#     index_main()
#     return FileResponse('plot.png')


def create_table_frequencies(data: dict):
    df=pd.DataFrame(data)
    print(df)


if __name__ == '__main__':
    n=10
    lista_datos = generate_data(n)
    
    numero_particiones=int(1+3.32*math.log10(n))
    rango = max(lista_datos)-min(lista_datos)
    amplitud=rango/numero_particiones
    intervalo=min(lista_datos)

    datos_dict = create_table(lista_datos, numero_particiones, intervalo, amplitud, n)
    generate_plot(lista_datos)
    calcular_datos_estadisticos(lista_datos)
    create_table_frequencies(datos_dict)
