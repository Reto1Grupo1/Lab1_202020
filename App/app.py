"""
 * Copyright 2020, Departamento de sistemas y ComputaciÃ³n, Universidad de Los Andes
 * 
 * ContribuciÃ³n de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este mÃ³dulo es una aplicaciÃ³n bÃ¡sica con un menÃº de opciones para cargar datos, contar elementos, y hacer bÃºsquedas sobre una lista.
"""

import config as cf
import sys
import csv
from time import process_time 

def loadCSVFile (file, lst, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file 
            Archivo de texto del cual se cargaran los datos requeridos.
        lst :: []
            Lista a la cual quedaran cargados los elementos despues de la lectura del archivo.
        sep :: str
            Separador escodigo para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    """
    del lst[:]
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")
    
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecuciÃ³n ",t1_stop-t1_start," segundos")

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos Movies casting")
    print("2- Cargar Datos Movies details")
    print("3- Saber cuantas buenas peliculas existen de un director")
    print("4- Conocer las peliculas mas/menos votadas y las mejores/peores votadas")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizarÃ¡ el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if len(lst)==0:
        print("La lista esta vacÃ­a")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0 #Cantidad de repeticiones
        for element in lst:
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecuciÃ³n ",t1_stop-t1_start," segundos")
    return counter

def encontrarbuenaspeliculas(director,listacasting,listadetails):
    listaid=[]
    totalcalificacion=0
    totalpeliculas=0
    
    for i in range(1,len(listacasting)):
        if listacasting[i]["director_name"]==director:
            listaid.append(listacasting[i]["id"])
            
    for i in range(1,len(listadetails)):
        if listadetails[i]["id"] in listaid:
            if float(listadetails[i]["vote_average"])>=6.0:
                totalcalificacion=totalcalificacion+float(listadetails[i]["vote_average"])
                totalpeliculas=totalpeliculas+1
                    
    promediocalificacion=round((totalcalificacion/totalpeliculas),2)
    
    texto="Su numero de peliculas buenas son: "+str(totalpeliculas)+". Su promedio de calificacion es: "+str(promediocalificacion)
    
    return texto

def rankingpeliculas(listadetails,masvotadas,menosvotadas,mejoresvotadas,peoresvotadas):
    listaaverage=[]
    listacount=[]
    retorno={}
    
    for i in range(1,len(listadetails)):
        listaaverage.append(listadetails[i]["vote_average"])
        listacount.append(listadetails[i]["vote_count"])
        
    if masvotadas==1:
        nombremaxcount=[]
        listacount=sorted(listacount)
        listacount=listacount[::-1]
        listamaxcount=(listacount[0:10])
        for i in range(0,len(listamaxcount)):
            for j in range(1,len(listadetails)):
                if int(listamaxcount[i])==int(listadetails[j]["vote_count"]) and listadetails[j]["title"] not in nombremaxcount and len(nombremaxcount)<10:
                    nombremaxcount.append(listadetails[j]["title"])
        retorno["mas_votadas"]=nombremaxcount
        
    if menosvotadas==1:
        nombremincount=[]
        listacount=sorted(listacount)
        listamincount=(listacount[0:10])
        for i in range(0,len(listamaxcount)):
            for j in range(1,len(listadetails)):
                if int(listamincount[i])==int(listadetails[j]["vote_count"]) and listadetails[j]["title"] not in nombremincount and len(nombremincount)<10:
                    nombremincount.append(listadetails[j]["title"])
        retorno["menos_votadas"]=nombremincount
        
    if mejoresvotadas==1:
        nombremaxaverage=[]
        listaaverage=sorted(listaaverage)
        listaaverage=listaaverage[::-1]
        listamaxaverage=(listaaverage[0:10])
        for i in range(0,len(listamaxaverage)):
            for j in range(1,len(listadetails)):
                if float(listamaxaverage[i])==float(listadetails[j]["vote_count"]) and listadetails[j]["title"] not in nombremaxaverage and len(nombremaxaverage)<10:
                    nombremaxaverage.append(listadetails[j]["title"])
        retorno["mejores_votadas"]=nombremaxaverage
        
    if peoresvotadas==1:
        nombreminaverage=[]
        listaaverage=sorted(listaaverage)
        listaminaverage=(listaaverage[0:10])
        for i in range(0,len(listaminaverage)):
            for j in range(1,len(listadetails)):
                if float(listaminaverage[i])==float(listadetails[j]["vote_count"]) and listadetails[j]["title"] not in nombreminaverage and len(nombreminaverage)<10:
                    nombreminaverage.append(listadetails[j]["title"])
        retorno["peores_votadas"]=nombreminaverage
        
    return retorno

def main():
    """
    MÃ©todo principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarÃ¡n los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    listacasting = [] #instanciar una lista vacia
    listadetails = []
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opciÃ³n para continuar\n') #leer opciÃ³n ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                loadCSVFile("Data/MoviesCastingRaw-small.csv", listacasting) #llamar funcion cargar datos
                print("Datos de casting cargados, "+str(len(listacasting))+" elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                loadCSVFile("Data/SmallMoviesDetailsCleaned.csv", listadetails) #llamar funcion cargar datos
                print("Datos de details cargados, "+str(len(listadetails))+" elementos cargados")
            elif int(inputs[0])==3: #opcion 3
               director=str(input("Escriba el nombre del director: "))
               print(encontrarbuenaspeliculas(director,listacasting,listadetails))
            elif int(inputs[0])==4: #opcion 4
                masvotadas=int(input("Desea conocer las 10 peliculas mas votadas? 1:Si, 0:no: "))
                menosvotadas=int(input("Desea conocer las 10 peliculas menos votadas? 1:Si, 0:no: "))
                mejoresvotadas=int(input("Desea conocer las 10 peliculas mejores votadas? 1:Si, 0:no: "))
                peoresvotadas=int(input("Desea conocer las 10 peliculas peores votadas? 1:Si, 0:no: "))
                print(rankingpeliculas(listadetails,masvotadas,menosvotadas,mejoresvotadas,peoresvotadas))
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

if __name__ == "__main__":
    main()