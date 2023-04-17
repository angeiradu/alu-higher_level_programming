#!/usr/bin/python3
"""script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!"""
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
     # Create a cursor
    cursor = conn.cursor()
    # EXECUTE A SQL Query
    cursor.execute("SELECT * FROM states WHERE name=%s", (sys.argv[4], ))
    
    # Fetch the result of query
    query_rows = cursor.fetchall()

    # Print each row of the result
    for row in query_rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
