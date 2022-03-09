import mysql.connector
try:
    conn = mysql.connector.connect(host = "localhost",user ="root", password = "root",database = "collegedb")
    print("connection successfully accepted")
    cursor = conn.cursor()
    query = "select * from studenttb"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
except mysql.connector.Error as msg:
    print(msg)
finally:
    conn.close()