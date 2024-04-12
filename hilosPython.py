import threading
import random
import time

def ejecutar(parametro1=10, parametro2=20):        
    print(f"Función ejecutar llamada con parámetros: parametro1={parametro1}, parametro2={parametro2}")

    # Función que realiza alguna tarea utilizando los parámetros recibidos




def ordenar_subvector(subvector, hilo):
    """
    Ordena un subvector y muestra el tiempo que lleva ordenarlo.
    """
    tiempo_inicio = time.time()
    subvector.sort()
    tiempo_fin = time.time()
    tiempo_ejecucion = tiempo_fin - tiempo_inicio
    print(f"Hilo {hilo}: Subvector ordenado (Tiempo: {tiempo_ejecucion} segundos)")





def dividir_vector(vector, num_hilos):
    """
    Divide un vector en subvectores para ser procesados por múltiples hilos.
    
    Usa
       Vector a dividir.
       Número de hilos a utilizar.
    Retorna
       Lista de subvectores.
    """
    longitud_subvector = len(vector) 
    subvectores = [vector[i:i+longitud_subvector] for i in range(0, len(vector), longitud_subvector)]
    return subvectores




def unir_vectores(subvectores):
    """
    Une varios subvectores en un solo vector.
    
    Usa
        Lista de subvectores.
    
    Retorna
        Vector unido.
    """
    vector_ordenado = [num for subvector in subvectores for num in subvector]
    return vector_ordenado





def ordenar_vector(vector, num_hilos):
    """
    Ordena un vector utilizando múltiples hilos.
    
    Usa
        Vector a ordenar.
        Número de hilos a utilizar.
    """
    subvectores = dividir_vector(vector, num_hilos)
    threads = []

    # Inicia un hilo para ordenar cada subvector
    for i, subvector in enumerate(subvectores):
        thread = threading.Thread(target=ordenar_subvector, args=(subvector, i))
        thread.start()
        threads.append(thread)
    
    # Espera a que todos los hilos terminen
    for thread in threads:
        thread.join()

    # Une los subvectores ordenados en un vector final
    vector_ordenado = unir_vectores(subvectores)
    print(f"Vector ordenado final: {vector_ordenado}")





# Generar un vector grande de números aleatorios
vector_grande = [random.randint(1, 10000) for _ in range(100000)]

# Obtener la cantidad de hilos desde la entrada del usuario
num_hilos = int(input("Ingrese la cantidad de hilos: "))

# Ordenar el vector utilizando la cantidad de hilos especificada 
# se agrego esto para hacer el ordenamiento correctamente no esta en el pdf 
ordenar_vector(vector_grande, num_hilos)



#Con respecto a las 2 preguntas 
#¿cómo solucionar el tema del ordenamiento?,
#Investigando y leyendo en diferentes sitios encontré lo siguiente:
#devolver el subvector ordenado al hilo principal que inició los hilos, permitiendo así que el hilo principal reúna todos los subvectores ordenados.
#una vez que el hilo principal haya recolectado todos los subvectores ordenados, puede unirlos 
#en un único vector ordenado final utilizando la función unir_vectores. Esto garantiza que el vector completo esté correctamente ordenado y listo para ser utilizado.

#Determinar el mejor número de hilos para este problema.
#Determinar el mejor número de hilos para este problema puede depender de diversos factores, como el tamaño del vector, 
#la complejidad del algoritmo de ordenamiento, el número de núcleos del procesador de cada computadora
#entre otros, se deberia de probar en el caso de cada computadora en el mio propiamente 
#el mejor rendimiento es utilizando 4 nucleos y 8 procesadores por lo tanto es la misma
# cantidadad de hilos y vectores para obtener el mejor numero.