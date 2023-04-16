#!/usr/bin/python3
import sys
import MySQLdb

args=sys.argv


# Connect to the database
db=MySQLdb.connect(
        host='localhost',
        port=3306,
        username=args[1],
        password=args[2],
        database=args[3]
        )

# Create a cursor for executing queries
cursor=db.cursor()

# Execute a query
cursor.execute("SELECT *FROM states ORDER BY states.id ASC")

#Fetch and print query results
for i in cursor.fetchall():
    print(i)

#Close the cursor and connection
cursor.close()
db.close()
