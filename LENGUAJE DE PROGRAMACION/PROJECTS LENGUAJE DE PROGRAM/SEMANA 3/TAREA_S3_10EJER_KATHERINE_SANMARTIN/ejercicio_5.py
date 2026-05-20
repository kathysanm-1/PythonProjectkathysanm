# =============================================================================
# EJERCICIO 5
# Tema: Bucle while
# Salida esperada:
# Apagado en: 5
# Apagado en: 4
# Apagado en: 3
# Apagado en: 2
# Apagado en: 1
# Apagando servidor...
#
# Objetivo:
# Realizar una cuenta regresiva utilizando un bucle while.
#
# Aprendizaje:
# - Uso del bucle while.
# - Manejo de variables de control.
# - Actualizacion de variables dentro del bucle.
# - Automatizacion de procesos repetitivos.
#
# Las cuentas regresivas son utilizadas en tareas automatizadas,
# apagado de servidores y ejecucion programada de procesos.
# =============================================================================

def ejercicio_5():

    print("\n--- EJERCICIO 5: CUENTA REGRESIVA ---")

    # Variable de control inicial
    contador = 5

    # El bucle se ejecuta mientras contador sea mayor o igual a 1
    while contador >= 1:

        print(f"Apagado en: {contador}")

        # Reducimos el valor del contador en cada vuelta
        contador -= 1

    # Mensaje final cuando el bucle termina
    print("Apagando servidor...")


# =============================================================================
# CONCLUSION DEL EJERCICIO
# =============================================================================
# En este ejercicio aprendi a utilizar el bucle while
# para repetir instrucciones mientras una condicion sea verdadera.
#
# Tambien comprendi la importancia de actualizar la variable
# de control para evitar bucles infinitos.
#
# Este tipo de procesos son utilizados en automatizacion
# y administracion de sistemas y servidores.
# =============================================================================


# Llamada de la funcion
ejercicio_5()