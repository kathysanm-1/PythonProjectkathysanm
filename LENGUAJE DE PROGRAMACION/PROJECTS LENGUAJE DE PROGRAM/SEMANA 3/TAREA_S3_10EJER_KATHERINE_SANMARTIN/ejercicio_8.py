# =============================================================================
# EJERCICIO 8
# Tema: Uso de continue
# Salida esperada:
# Procesando: 10.0.0.5
# Procesando: 10.0.0.8
# Procesando: 10.0.0.10
# Total procesadas: 3
# Pista: Al inicio del bloque del for,
#
# Objetivo:
# Filtrar direcciones IP ignorando aquellas que esten
# dentro de una lista negra.
#
# Aprendizaje:
# - Uso del bucle for.
# - Uso de continue para saltar iteraciones.
# - Uso de contadores.
# - Validacion y filtrado de datos.
#
# En ciberseguridad es comun bloquear o ignorar IPs
# sospechosas mediante listas negras (blacklists).
# =============================================================================

def ejercicio_8():

    print("\n--- EJERCICIO 8: FILTRAR IPS ---")

    # Lista de IPs registradas en logs
    ips_log = [
        "10.0.0.5",
        "200.0.0.1",
        "10.0.0.8",
        "45.33.32.156",
        "10.0.0.10"
    ]

    # Lista negra de IPs bloqueadas
    blacklist = [
        "200.0.0.1",
        "45.33.32.156"
    ]

    # Contador de IPs procesadas
    total = 0

    # Recorrer todas las IPs
    for ip in ips_log:

        # Si la IP esta en la blacklist
        if ip in blacklist:

            # continue salta esta iteracion
            # y pasa a la siguiente IP
            continue

        # Solo se ejecuta si la IP NO esta bloqueada
        print(f"Procesando: {ip}")

        # Aumentamos el contador
        total += 1

    # Resultado final
    print(f"Total procesadas: {total}")


# =============================================================================
# CONCLUSION DEL EJERCICIO
# =============================================================================
# En este ejercicio aprendi a utilizar continue
# para omitir elementos especificos dentro de un bucle.
#
# Tambien comprendi como filtrar informacion
# utilizando listas negras y contadores.
#
# Este tipo de procesos son utilizados en sistemas
# de seguridad y monitoreo de trafico de red.
# =============================================================================


# Llamada de la funcion
ejercicio_8()