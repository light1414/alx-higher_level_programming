#!/usr/bin/python3
"""
Shows the values in the states table of the database hbtn_0e_0_usa
matching the supplied argument.
Safe from SQL injections.
Usage: ./my_safe_filter_states.py <mysql username> <mysql password>
                                  <database name> <state name searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM `states`")
    [print(state) for state in curs.fetchall() if state[1] == sys.argv[4]]
