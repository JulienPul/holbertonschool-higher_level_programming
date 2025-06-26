#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa,
along with their corresponding state name.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get credentials from command line
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()
    # One single execute()
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
