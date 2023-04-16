#!/usr/bin/python3
# import module
import MySQLdb
from sys import argv

# arguments
username = argv[1]
password = argv[2]
database = argv[3]

# connect to database
db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=database
    )

# create cursor
cursor = db.cursor()

# execute query
cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

# fetch all rows
rows = cursor.fetchall()

# loop through rows
for row in rows:
    print(row)

# close connection
cursor.close()
db.close()
