#!/usr/bin/python3
"""
Lists all cities of a given state from the database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username, password, db_name, state_name = sys.argv[1:5]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()

    # IMPORTANT: no triple quotes for the query
    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s ORDER BY cities.id"
    )

    cur.execute(query, (state_name,))

    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))

    cur.close()
    db.close()
