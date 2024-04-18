import threading
import random
import time

def ejecutar(parametro1=10, parametro2=20):        
    print(f"Funci�n ejecutar llamada con par�metros: parametro1={parametro1}, parametro2={parametro2}")


def ordenar_subvector(subvector, hilo):
    tiempo_inicio = time.time()
    subvector.sort()
    tiempo_fin = time.time()
    tiempo_ejecucion = tiempo_fin - tiempo_inicio
    print(f"Hilo {hilo}: Subvector ordenado (Tiempo: {tiempo_ejecucion} segundos)")


def dividir_vector(vector, num_hilos):
    longitud_subvector = len(vector) // num_hilos
    subvectores = [vector[i:i+longitud_subvector] for i in range(0, len(vector), longitud_subvector)]
    return subvectores


def unir_vectores(subvectores):
    vector_ordenado = [num for subvector in subvectores for num in subvector]
    return vector_ordenado


def ordenar_vector(vector, num_hilos):
    subvectores = dividir_vector(vector, num_hilos)
    threads = []

    for i, subvector in enumerate(subvectores):
        thread = threading.Thread(target=ordenar_subvector, args=(subvector, i))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

    vector_ordenado = unir_vectores(subvectores)
    print(f"Vector ordenado final: {vector_ordenado}")
    if vector_ordenado == vector_grande.sort():
        print(f"ES IGUAL")
    else:
        print(f"NO ES IGUAL")


vector_grande = [random.randint(1, 10000) for _ in range(10000)]

num_hilos = int(input("Ingrese la cantidad de hilos: "))

ordenar_vector(vector_grande, num_hilos)



#Con respecto a las 2 preguntas 
#�c�mo solucionar el tema del ordenamiento?,
#Investigando y leyendo en diferentes sitios encontr� lo siguiente:
#devolver el subvector ordenado al hilo principal que inici� los hilos, permitiendo as� que el hilo principal re�na todos los subvectores ordenados.
#una vez que el hilo principal haya recolectado todos los subvectores ordenados, puede unirlos 
#en un �nico vector ordenado final utilizando la funci�n unir_vectores. Esto garantiza que el vector completo est� correctamente ordenado y listo para ser utilizado.

#Determinar el mejor n�mero de hilos para este problema.
#Determinar el mejor n�mero de hilos para este problema puede depender de diversos factores, como el tama�o del vector, 
#la complejidad del algoritmo de ordenamiento, el n�mero de n�cleos del procesador de cada computadora
#entre otros, se deberia de probar en el caso de cada computadora en el mio propiamente 
#el mejor rendimiento es utilizando 4 nucleos y 8 procesadores por lo tanto es la misma
# cantidadad de hilos y vectores para obtener el mejor numero.