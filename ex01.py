import mysql.connector
try:
    conn = mysql.connector.connect(host = "localhost",user = "root",password = "root",database = "collegedb")
    print("connection succesfully established")
except mysql.connector.Error as msg:
    print(msg)
finally:
    conn.close()