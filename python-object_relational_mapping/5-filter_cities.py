#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
                           
    # Create a cursor
    cursor = db.cursor()
    # Execute SQL Query
    cursor.execute("SELECT cities.name FROM cities\
        JOIN states ON cities.state_id = states.id\
            WHERE states.name=%s", (sys.argv[4], ))

    query_rows = cursor.fetchall()
    out = []
    for row in query_rows:
        out.append(row[0])
    # Print query
    print(', '.join(out))

    # Close cursor and connection
    cursor.close()
    db.close()
