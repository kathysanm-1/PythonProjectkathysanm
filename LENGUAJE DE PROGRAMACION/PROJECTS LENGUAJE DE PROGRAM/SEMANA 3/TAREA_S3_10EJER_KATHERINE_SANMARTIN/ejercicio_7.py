# =============================================================================
# EJERCICIO 7
# Tema: Uso de break
# Salida esperada:
# Puerto 21: abierto
# Puerto 22: abierto
# Puerto 23: abierto
# Primer puerto cerrado: 25
#
# Objetivo:
# Detectar el primer puerto cerrado y detener el recorrido.
#
# Aprendizaje:
# - Uso del bucle for.
# - Uso de zip() para recorrer listas en paralelo.
# - Uso de break para salir de un bucle.
# - Evaluacion de condiciones dentro de iteraciones.
#
# Durante un escaneo de red es comun detener procesos
# cuando se detecta un evento importante o un error.
# =============================================================================

def ejercicio_7():

    print("\n--- EJERCICIO 7: PRIMER PUERTO CERRADO ---")

    # Lista de puertos
    puertos = [21, 22, 23, 25, 80]

    # Estado de cada puerto
    estados = ["abierto", "abierto", "abierto", "cerrado", "abierto"]

    # zip() une ambas listas para recorrerlas juntas
    for puerto, estado in zip(puertos, estados):

        # Si el puerto esta cerrado
        if estado == "cerrado":

            print(f"Primer puerto cerrado: {puerto}")

            # break detiene inmediatamente el bucle
            break

        # Si esta abierto se muestra normalmente
        print(f"Puerto {puerto}: {estado}")


# =============================================================================
# CONCLUSION DEL EJERCICIO
# =============================================================================
# En este ejercicio aprendi a utilizar break
# para detener un bucle cuando se cumple una condicion.
#
# Tambien comprendi el uso de zip() para recorrer
# dos listas al mismo tiempo.
#
# Este tipo de logica es utilizada en escaneos
# y monitoreo de puertos en redes.
# =============================================================================


# Llamada de la funcion
ejercicio_7()