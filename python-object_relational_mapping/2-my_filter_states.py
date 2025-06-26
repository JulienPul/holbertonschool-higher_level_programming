#!/usr/bin/python3
"""
Lists all states where name matches the argument from the database hbtn_0e_0_usa.
Usage: ./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Arguments en ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Création du curseur
    cur = db.cursor()

    # Requête SQL avec format (non sécurisé - volontaire)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Affichage des résultats
    for row in cur.fetchall():
        print(row)

    # Fermeture
    cur.close()
    db.close()
