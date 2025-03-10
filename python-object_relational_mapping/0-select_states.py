#!/usr/bin/python3
"""
Este script se conecta a una base de datos MySQL, ejecuta una consulta para obtener 
todos los registros de la tabla 'states' ordenados por el campo 'id', e imprime los resultados.

Parámetros:
    El script acepta tres parámetros desde la línea de comandos:
        - mysql_user: Nombre de usuario para conectarse a la base de datos MySQL.
        - mysql_pass: Contraseña del usuario de la base de datos MySQL.
        - db_name: Nombre de la base de datos a la que se conecta.

Requiere:
    - MySQLdb (para conectarse a la base de datos MySQL).
    - sys (para obtener los argumentos de línea de comandos).

Uso:
    python3 script.py <mysql_user> <mysql_pass> <db_name>
    Ejemplo:
        python3 script.py root mypassword mydatabase
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_pass,
        db=db_name
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()