#!/usr/bin/python3
"""
Este script se conecta a una base de datos MySQL
"""
import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC"
    ).format(state_name)

    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
