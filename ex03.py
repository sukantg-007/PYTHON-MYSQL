import mysql.connector
def getRecord():
    try:
        conn = mysql.connector.connect(host = "localhost",user ="root", password = "root",database = "collegedb")
        #print("connection successfully accepted")
        cursor = conn.cursor()
        query = "select * from studenttb"
        cursor.execute(query)
        t=cursor.fetchall()      
    except mysql.connector.Error as msg:
        print(msg)
    finally:
        conn.close()
    return t

allRecord=getRecord()
print(type(allRecord))