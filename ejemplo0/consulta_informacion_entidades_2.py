"""
    Consulta de información en las entidades en la base de datos
"""

from base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute


# hace consultas a la base de datos
cadena_consulta_sql = "SELECT * from Autor"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

print(informacion)
# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
print("******************************************************************************")
for d in informacion:
    print(f"El nombre es {d[0]} y su edad es {d[3]}")
#     print("%s - %s - %s - %d" % (d[0], d[1], d[2], d[3]))
# Lo que se hizo en este archivo es la lectura de una base de datos sqlite, teniendo como respesta una lista de tuplas,
# para imprimir esta información vamos a recorrercada una de las tuplas y a su vez, cada elemento que contenga las tuplas,
# obteniendo el resultado que se ve en pantalla al ejecutar este ejercicio.
# Hay que tener en cuenta la siguiente información acerca de los tipos de datos
# {}: Diccionario
# []: Lista
# (): Tupla


# cerrar el enlace a la base de datos (recomendado)
cursor.close()
