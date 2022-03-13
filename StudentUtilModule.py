import mysql.connector
from studentinfo import Student

class StudentUtil:
    conn = mysql.connector.connect(host = "localhost",user ="root", password = "root",database = "collegedb")        
    cursor = conn.cursor()

    @staticmethod
    def getallstd():
        try:        
            query = "select * from studenttb"
            StudentUtil.cursor.execute(query)
            t=StudentUtil.cursor.fetchall()      
        except mysql.connector.Error as msg:
            print(msg)    
        return t

    @staticmethod
    def getstdbyid(id):
        try:        
            query = "select * from studenttb where id={}".format(id)
            StudentUtil.cursor.execute(query)
            t=StudentUtil.cursor.fetchone()
            return t if t else "Record not found"
        except mysql.connector.Error as msg:                        
            return msg

    @staticmethod
    def stdupdate(id):
        try:
            query = "select * from studenttb where id = {}".format(id)
            StudentUtil.cursor.execute(query)
            t = StudentUtil.cursor.fetchone()
            if t:
                new_name = input("Enter name to update :")
                query = "update studenttb set sname='{}' where id={}".format(new_name,id)
                StudentUtil.cursor.execute(query)
                return "Successfully Updated"
            else:
                return "No record found"
        except mysql.connector.Error as msg:
            print(msg)

    @staticmethod
    def Savestudent(std):
        try:
            query = "INSERT INTO STUDENTTB VALUES ({},'{}','{}','{}')".format(std.id,std.sname,std.saddr,std.sclass)
            StudentUtil.cursor.execute(query)
            StudentUtil.conn.commit()
            return "Succeessfully inserted"
        except mysql.connector.Error as msg:
            return msg 
    
    @staticmethod
    def deletestd(id):
        #delete student
        pass