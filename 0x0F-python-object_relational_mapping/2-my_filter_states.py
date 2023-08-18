#!/usr/bin/python3
"""
Displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mySQLi

    try:
        db = mySQLi.connect(host='localhost', user=argv[1], port=3306,
                           passwd=argv[2], db=argv[3])
    except Exception:
        print('Failed to connect to the database')
        exit(0)

    searched = argv[4]
    cursors = db.cursor()
    cursors.execute("SELECT * FROM states WHERE name = BINARY '{:s}' \
                    ORDER BY id ASC;".format(searched))
    query_result = cursors.fetchall()

    for row in query_result:
        print(row)

    cursors.close()
    db.close()
