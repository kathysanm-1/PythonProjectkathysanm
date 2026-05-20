# =============================================================================
# EJERCICIO 2
# Tema: if / elif / else
# Salida esperada:
# puerto = 443 -> Puerto 443: HTTPS
# puerto = 8080 -> Puerto 8080: Servicio desconocido
#
# Objetivo:
# Identificar el servicio de red asociado a un numero de puerto.
#
# Aprendizaje:
# - Uso de multiples condiciones con elif.
# - Comparacion de numeros enteros.
# - Uso de variables para almacenar resultados.
# - Relacion entre puertos y servicios de red.
#
# Los puertos permiten identificar servicios activos en un servidor.
# En auditorias y escaneos de red es importante reconocerlos.
# =============================================================================

def ejercicio_2():

    print("\n--- EJERCICIO 2: IDENTIFICAR SERVICIO ---")

    # Variable que almacena el puerto a analizar
    puerto = 443

    # Evaluamos el puerto usando condicionales

    if puerto == 22:

        servicio = "SSH"

    elif puerto == 80:

        servicio = "HTTP"

    elif puerto == 443:

        servicio = "HTTPS"

    elif puerto == 3306:

        servicio = "MySQL"

    elif puerto == 3389:

        servicio = "RDP"

    # Si el puerto no coincide con ninguno conocido
    else:

        servicio = "Servicio desconocido"

    # Mostrar resultado final
    print(f"Puerto {puerto}: {servicio}")


# =============================================================================
# CONCLUSION DEL EJERCICIO
# =============================================================================
# En este ejercicio aprendi a utilizar estructuras if, elif y else
# para evaluar multiples condiciones.
#
# Tambien comprendi como relacionar numeros de puerto con
# servicios de red utilizados en redes y ciberseguridad.
#
# Este tipo de logica es utilizada en escaneos y analisis
# de servicios activos dentro de una red.
# =============================================================================


# Llamada de la funcion
ejercicio_2()