#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Get username, password and database name from command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to database
    db = MySQLdb.connect(host = "localhost", port = 3306, user = username, passwd = password, db = database)

    # Get a cursor object
    cursor = db.cursor()

    # Execute query
    cursor.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities \
                    INNER JOIN states \
                    ON states.id = cities.state_id \
                    ORDER BY cities.id ASC")

    # Get results
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)
        
    # Close connection
    cursor.close()
    db.close()
