#!/usr/bin/python3
"""
Lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
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

    cursors = db.cursor()
    cursors.execute("SELECT * FROM states \
                    WHERE name LIKE BINARY 'N%' ORDER BY id ASC;")
    result_query = cursors.fetchall()

    for row in result_query:
        print(row)

    cursors.close()
    db.close()
