""" 
Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, escriba un
programa que manipule dichas estructuras de datos para poder resolver los siguientes puntos:
A. Generar una estructura con todas las notas relacionando el nombre del estudiante con las
notas. Utilizar esta estructura para la resolución de los siguientes items.
B. Calcular el promedio de notas de cada estudiante.
C. Calcular el promedio general del curso.
D. Identificar al estudiante con la nota promedio más alta.
E. Identificar al estudiante con la nota más baja.

"""
# Nombres de todos los estudiantes del curso
nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David',
'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 
'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge',
'JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa', 
'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás', 'Nancy', 'Noelia', 'Pablo', 
'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''

# Lista con la primer nota de cada estudiante
notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12, 77, 
           13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18, 7, 
           74, 60, 9, 65, 93, 63, 74]

# Lista con la segunda nota de cada estudiante
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64, 13, 8,
           87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15, 31,
           39, 15, 74, 33, 57, 10] 

def incisoA(nombres,notas_1,notas_2):
    """
    Genera una estructura con los nombres de los estudiantes del curso y sus respectivas notas.
    
    Args:
        nombres(string): Cadena con los nombres de los estudiantes del curso.
        notas_1(list): Lista con la primer nota de cada estudiante.
        notas_2(list): Lista con la segunda nota de cada estudiante.
        
    Returns:
        dicc_estudiantes(dict): Diccionario donde las claves son los nombres de los estudiantes y los valores son las notas de cada
        estudiante.
        
    """
    lista_notas = list(zip(notas_1,notas_2))
    names = nombres.replace("\n","").replace("'","").replace(" ","").strip().split(",")
    dicc_estudiantes = dict(zip(names,lista_notas))
    
    return dicc_estudiantes

def incisoB(diccionario_estudiantes):   
    """
    Calcula el promedio de las notas de cada estudiante y los guarda en un diccionario.
     
    Args:
        diccionario_estudiantes(dict): Diccionario con los nombres de los estudiantes y sus respectivas notas.

    Returns:
        dict_notas_promedios(dict): Diccionario con los nombres de los estudiantes y el promedio de sus notas.
    """
    
    promedios = list(map( lambda x: (x[0]+x[1])/2,diccionario_estudiantes.values()))
    dict_notas_promedios = dict(zip(diccionario_estudiantes.keys(),promedios))
    
    return dict_notas_promedios
    
def incisoC(diccionario_estudiantes):
    """
    Esta función calcula el promedio general de las notas del curso.

    Args:
        diccionario_estudiantes(dict): Diccionario con los nombres de los estudiantes y sus respectivas notas.

    Returns:
        promedio_notas_curso(float): Número flotante con el promedio general del curso.
    """
    
    suma_notas = sum([x+y for x,y in diccionario_estudiantes.values()])
    promedio_notas_curso = round((suma_notas / (int(len(diccionario_estudiantes.values()) * 2))),2)
    
    return promedio_notas_curso

def incisoD(diccionario_notas_promedio):  
    """
    Esta función identifica al estudiante con la nota promedio más alta.

    Args:
        diccionario_notas_promedio(dict): Diccionario con los nombres de los estudiantes y el promedio de sus notas.

    Returns:
        estudiante_nota_promedio_mas_alta(string): Nombre del estudiante con la nota promedio más alta.

    """
    estudiante_nota_promedio_mas_alta = max(diccionario_notas_promedio, key= diccionario_notas_promedio.get)
    
    return estudiante_nota_promedio_mas_alta

def incisoE(diccionario_estudiantes):
    """
    Esta función identifica al estudiante con la nota más baja del curso.

    Args:
        diccionario_estudiantes(dict): Diccionario con los nombres de los estudiantes y sus respectivas notas.

    Returns:
        estudiante_nota_mas_baja(string): Nombre del estudiante con la nota más baja del curso.

    """
    estudiante_nota_mas_baja = min(diccionario_estudiantes, key = diccionario_estudiantes.get )
    
    return estudiante_nota_mas_baja  
    
# Guardo en una variable el diccionario de los estudiantes con sus respectivas notas ya que lo voy a volver a utilizar como parámetro en otras funciones    
diccionario_estudiantes = incisoA(nombres,notas_1,notas_2)
# Guardo en una variable el diccionario de los estudiantes con el promedio de sus notasya que lo voy a volver a utilizar como parámetro en otras funciones
diccionario_notas_promedio = incisoB(diccionario_estudiantes)
# Guardo en una variable el alumno con la nota promedio más alta de todo el curso para imprimir su nota
estudiante_mayor_nota_promedio = incisoD(diccionario_notas_promedio)
# Guardo en una variable el alumno con la nota más baja de todo el curso para imprimir su nota
estudiante_peor_nota = incisoE(diccionario_estudiantes)
# Imprimo los estudiantes del curso con sus respectivas notas
print("-" * 100)
print('Alumnos del curso con sus respectivas notas:')
print(incisoA(nombres,notas_1,notas_2),"\n")
print("-" * 100)
# Imprimo el promedio de las notas de cada estudiante
print("-" * 100)
print('El promedio de las notas de cada estudiante es:')
print(incisoB(diccionario_estudiantes),"\n")
print("-" * 100)
# Imprimo el promedio general del curso
print('El promedio general del curso es:',incisoC(diccionario_estudiantes))
# Imprimo el estudiante con la nota promedio más alta de todo el curso y su respectiva nota
print('El estudiante con la nota promedio más alta es', incisoD(diccionario_notas_promedio),'con una nota de:',diccionario_notas_promedio.get(estudiante_mayor_nota_promedio))
# Imprimo el estudiante con la nota más baja de todo el curso y su respectiva nota
print('El estudiante con la nota más baja es', incisoE(diccionario_estudiantes),'con una nota de:',min(diccionario_estudiantes.get(estudiante_peor_nota)))
