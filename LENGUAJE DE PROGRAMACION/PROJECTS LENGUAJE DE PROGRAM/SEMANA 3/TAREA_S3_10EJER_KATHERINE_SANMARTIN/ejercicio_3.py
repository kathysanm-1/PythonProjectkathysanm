# =============================================================================
# EJERCICIO 3
# Tema: Bucle for con range()
# Salida esperada:
# 192.168.1.0
# 192.168.1.1
# 192.168.1.2
# ...
# 192.168.1.7
#
# Objetivo:
# Mostrar todas las direcciones IP de una subred utilizando
# un bucle for.
#
# Aprendizaje:
# - Uso del bucle for.
# - Uso de range() para generar secuencias numericas.
# - Uso de f-strings para construir texto dinamico.
# - Automatizacion de tareas repetitivas.
#
# Los recorridos de IPs son utilizados en escaneos de red,
# monitoreo y descubrimiento de dispositivos.
# =============================================================================

def ejercicio_3():

    print("\n--- EJERCICIO 3: LISTAR IPS DE UNA SUBRED ---")

    # range(8) genera numeros desde 0 hasta 7
    # Cada numero sera utilizado para formar la IP

    for i in range(8):

        # Construccion dinamica de la direccion IP
        print(f"192.168.1.{i}")


# =============================================================================
# CONCLUSION DEL EJERCICIO
# =============================================================================
# En este ejercicio aprendi a utilizar el bucle for para
# repetir instrucciones automaticamente.
#
# Tambien comprendi como usar range() para generar secuencias
# numericas y construir direcciones IP mediante f-strings.
#
# Este tipo de procesos son utilizados para escaneo
# y administracion de dispositivos conectados.
# =============================================================================


# Llamada de la funcion
ejercicio_3()