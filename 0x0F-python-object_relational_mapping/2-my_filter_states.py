#!/usr/bin/python3
"""
Shows all values in the states table of the database hbtn_0e_0_usa
matching the supplied as argument.
Usage: ./filter_states.py <mysql username>
                          <mysql password>
                          <database name>
                          <state name searched>
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db_connects = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )
    cur = db_connects.curs()
    cur.execute("SELECT * \
                     FROM `states` \
                     WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    states = cur.fetchall()
    [print(state) for state in states]
