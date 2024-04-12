
# ¿Cómo solucionar el tema del ordenamiento?,
Investigando y leyendo en diferentes sitios encontré lo siguiente:
devolver el subvector ordenado al hilo principal que inició los hilos, permitiendo así que el hilo principal reúna todos los subvectores ordenados.
una vez que el hilo principal haya recolectado todos los subvectores ordenados, puede unirlos 
en un único vector ordenado final utilizando la función unir_vectores. Esto garantiza que el vector completo esté correctamente ordenado y listo para ser utilizado.

# Determinar el mejor número de hilos para este problema.
Determinar el mejor número de hilos para este problema puede depender de diversos factores, como el tamaño del vector, 
la complejidad del algoritmo de ordenamiento, el número de núcleos del procesador de cada computadora
entre otros, se deberia de probar en el caso de cada computadora en el mio propiamente 
el mejor rendimiento es utilizando 4 nucleos y 8 procesadores por lo tanto es la misma
cantidadad de hilos y vectores para obtener el mejor numero.
