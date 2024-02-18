#!/usr/bin/python3
"""list all rows form the states table"""
import MySQLdb
import sys


def states_list(username, passwrod, database, name):
    """list all rows from the states table
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

    query = "SELECT * FROM states WHERE  name={} ORDER BY id ASC".format(name)
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username, password, database, name = sys.argv[1:]
        states_list(username, password, database, name)
