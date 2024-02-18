#!/usr/bin/python3
import MySQLdb
import sys

def states_list(username, passwrod, db_name):
    db = MySQLdb.connect(host='localhost',
                    port=3306,
                    user=username,
                    passwd=passwrod,
                    db=db_name)
    cur = db.cursor()

    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)

    rows =    cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, database = sys.argv[1:]
        states_list(username, password, database)
