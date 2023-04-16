#!/usr/bin/python3
# import the MySQLdb module
import MySQLdb
# takes 3 arguments
from sys import argv

username = argv[1]
password = argv[2]
database = argv[3]

# connect to the MySQL server
db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=database
)

# create a cursor object
cur = db.cursor()

# execute a query
cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

# fetch all rows
rows = cur.fetchall()

# print rows
for row in rows:
    print(row)

# close the cursor
cur.close()

# close the connection
db.close()
