#!/usr/bin/python3
"""connect with a mysql database"""
import MySQLdb
import sys


def states_list(username, passwrod, database, name):
    """runs some sql
        Args:
        username: the username for the database
        passwrod: the password for the database
        db_name: the name of the database
    """
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=passwrod,
        db=database)
    cur = db.cursor()

    query = "SELECT cities.name FROM cities\
            join states on states.id = cities.state_id\
            WHERE  states.name=%s ORDER BY cities.id ASC"
    cur.execute(query, (name,))

    rows = cur.fetchall()

    result = ", ".join(row[0] for row in rows)
    print(result)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username, password, database, name = sys.argv[1:]
        states_list(username, password, database, name)
