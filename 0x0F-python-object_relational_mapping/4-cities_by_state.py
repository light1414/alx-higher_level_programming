#!/usr/bin/python3
"""
Defines cities of the database hbtn_0e_4_usa, thats ordered by city id.
Use: ./4-cities_by_state.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db_username, db_password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(user=db_username, passwd=db_password, db=db_name)
    cur = db.cursor()

    cur.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                     FROM `cities` as `c` \
                     INNER JOIN `states` as `s` \
                     ON `c`.`state_id` = `s`.`id` \
                     ORDER BY `c`.`id`")

    [print(city) for city in cur.fetchall()]

    cur.close()
    db.close()
