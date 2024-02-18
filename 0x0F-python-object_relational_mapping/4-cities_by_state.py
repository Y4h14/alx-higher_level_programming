#!/usr/bin/python3
"""list all rows form the cities table"""
import MySQLdb
import sys


def states_list(username, passwrod, database):
    """list all rows from the cities table
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

    query = "SELECT * FROM cities ORDER BY id ASC"
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, database = sys.argv[1:]
        states_list(username, password, database)
