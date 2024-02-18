#!/usr/bin/python3
"""connect with a mysql database"""
import MySQLdb
import sys


def run_sql(username, passwrod, database, name):
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

    query = "SELECT * FROM states WHERE  name=%s ORDER BY id ASC"
    cur.execute(query, (name,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username, password, database, name = sys.argv[1:]
        run_sql(username, password, database, name)
