# =============================================================================
# EJERCICIO 6
# Tema: while con condicion compuesta
# Salida esperada:
# Intento 1: sin respuesta
# Intento 2: sin respuesta
# Intento 3: CONECTADO
#
# Objetivo:
# Simular el reintento de conexion a un servidor.
#
# Aprendizaje:
# - Uso del bucle while.
# - Uso de variables booleanas.
# - Uso de condiciones compuestas con and y not.
# - Simulacion de procesos de conexion.
#
# Los sistemas y servidores realizan multiples intentos
# de conexion antes de cancelar una comunicacion.
# =============================================================================

def ejercicio_6():

    print("\n--- EJERCICIO 6: REINTENTO DE CONEXION ---")

    # Variable que controla el numero de intentos
    intento = 1

    # Estado inicial de la conexion
    conectado = False

    # El bucle se ejecuta:
    # - mientras el intento sea menor o igual a 5
    # - y mientras NO exista conexion

    while intento <= 5 and not conectado:

        # Simulamos que la conexion se logra en el intento 3
        if intento == 3:

            conectado = True

            print(f"Intento {intento}: CONECTADO")

        else:

            print(f"Intento {intento}: sin respuesta")

        # Aumentamos el numero de intento
        intento += 1


# =============================================================================
# CONCLUSION DEL EJERCICIO
# =============================================================================
# En este ejercicio aprendi a utilizar condiciones
# compuestas dentro de un bucle while.
#
# Tambien comprendi el uso de variables booleanas
# para controlar estados de conexion.
#
# Este tipo de logica es utilizada en sistemas,
# servidores y procesos de autenticacion en redes.
# =============================================================================


# Llamada de la funcion
ejercicio_6()