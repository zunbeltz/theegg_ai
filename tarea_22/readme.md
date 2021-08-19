# Tarea 22: El algoritmo del lechero

En este problema tenemos un conjunto de vacas. Cada vaca tiene 2
propiedades: peso y litro de leche producidos por día.  El objetivo es
seleccionar un número de vacas que maximicen la producción de leche
manteniendo el peso total por debajo del límite permitido por el
camión.

## Fuerza bruta
La solución más simple es el de fuerza bruta; es decir, computar todas
las combinaciones de vacas que pueden entrar en el camión, y de
aquellas que cumplan la condición de peso escoger la de mayor cantidad
de leche.

El fichero cow_force.py muestra este algoritmo.

## Programación lineal
Este problema es muy conocido en el ámbito de la optimización y la
programación lineal. Es conocido como el problema de la mochila y
puede obtenerse una solución usando el algoritmo simplex o algún tipo
de "bound and cut".

El fichero cow_pulp.py muestra el uso de la librería de programación 
lineal pulp en este problema
