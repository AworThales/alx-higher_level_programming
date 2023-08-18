#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mySQLi

    if (len(argv) != 4):
        print('Use: username, password, database name')
        exit(1)

    try:
        db = mySQLi.connect(host='localhost', user=argv[1], port=3306,
                           passwd=argv[2], db=argv[3])
    except Exception:
        print('Failed to connect to the database')
        exit(0)

    cursors = db.cursor()
    cursors.execute("""SELECT c.id, c.name, s.name FROM cities as c
                      INNER JOIN states as s
                      ON c.state_id = s.id
                      ORDER BY c.id ASC;""")
    query_result = cursors.fetchall()
    for row in query_result:
        print(row)
    cursors.close()
    db.close()
