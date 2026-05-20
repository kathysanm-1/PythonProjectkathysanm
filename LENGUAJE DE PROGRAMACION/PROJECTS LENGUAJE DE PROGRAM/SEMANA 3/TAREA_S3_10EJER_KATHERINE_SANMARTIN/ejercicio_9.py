# =============================================================================
# EJERCICIO 9
# Tema: else en un bucle for
# Salida esperada:
# buscar = "Firewall-FW1" -> Encontrado
# buscar = "Switch-Z" -> No encontrado en el inventario
#
# Objetivo:
# Buscar un dispositivo dentro de un inventario utilizando
# un bucle for y la clausula else.
#
# Aprendizaje:
# - Uso del bucle for.
# - Uso de break.
# - Uso de else en bucles.
# - Busqueda de elementos dentro de listas.
#
# Los inventarios son utilizados para administrar equipos
# y verificar la existencia de dispositivos en una red.
# =============================================================================

def ejercicio_9():

    print("\n--- EJERCICIO 9: BUSCAR DISPOSITIVO ---")

    # Lista de dispositivos del inventario
    inventario = [
        "Router-01",
        "Switch-A",
        "Firewall-FW1",
        "Servidor-Web"
    ]

    # Dispositivo que queremos buscar
    buscar = "Firewall-FW1"

    # Recorrer el inventario
    for dispositivo in inventario:

        # Verificar si el dispositivo coincide
        if dispositivo == buscar:

            print(f"{buscar} -> Encontrado")

            # Salimos inmediatamente del bucle
            break

    # Este else pertenece al FOR, no al IF
    # Solo se ejecuta si NO hubo break
    else:

        print(f"{buscar} -> No encontrado en el inventario")


# =============================================================================
# CONCLUSION DEL EJERCICIO
# =============================================================================
# En este ejercicio aprendi a utilizar la clausula else
# dentro de un bucle for.
#
# Tambien comprendi como realizar busquedas dentro
# de listas utilizando break para detener el recorrido.
#
# Este tipo de logica es utilizada en inventarios,
# monitoreo y administracion de dispositivos de red.
# =============================================================================


# Llamada de la funcion
ejercicio_9()