# =============================================================================
# EJERCICIO 4
# Tema: for con enumerate()
# Salida esperada:
# 1. Router Cisco
# 2. Switch HP
# 3. Firewall Fortinet
# 4. Servidor Dell
#
# Objetivo:
# Recorrer una lista de dispositivos mostrando cada elemento
# con una numeracion automatica.
#
# Aprendizaje:
# - Uso del bucle for con listas.
# - Uso de enumerate().
# - Manipulacion de posiciones e indices.
# - Presentacion ordenada de informacion.
#
# En administracion de redes es comun trabajar con inventarios
# de dispositivos como routers, switches y firewalls.
# =============================================================================

def ejercicio_4():

    print("\n--- EJERCICIO 4: INVENTARIO DE DISPOSITIVOS ---")

    # Lista de dispositivos de red
    dispositivos = [
        "Router Cisco",
        "Switch HP",
        "Firewall Fortinet",
        "Servidor Dell"
    ]

    # enumerate() permite obtener:
    # - la posicion
    # - el valor de cada elemento

    for posicion, valor in enumerate(dispositivos, start=1):

        print(f"{posicion}. {valor}")


# =============================================================================
# CONCLUSION DEL EJERCICIO
# =============================================================================
# En este ejercicio aprendi a recorrer listas utilizando
# el bucle for junto con enumerate().
#
# Tambien comprendi como mostrar informacion organizada
# mediante posiciones numeradas.
#
# Este tipo de estructuras son utiles para administrar
# inventarios y dispositivos dentro de una red.
# =============================================================================


# Llamada de la funcion
ejercicio_4()