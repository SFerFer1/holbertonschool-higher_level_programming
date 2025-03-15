#!/usr/bin/python3
"""
Este script se conecta a una base de datos MySQL
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]
    search_term = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_pass,
        db=db_name
    )

    cursor = db.cursor()


    query = "SELECT * FROM states WHERE BINARY name LIKE %s ORDER BY id ASC"
    cursor.execute(query, (search_term,))

    states = cursor.fetchall()


    if len(states) == 0:
        sys.exit(0)

    for state in states:
        print(state)

    cursor.close()
    db.close()

