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
    def stdupdate(id,**kwargs):  
        try:
            query = "select * from studenttb where id = {}".format(id)
            StudentUtil.cursor.execute(query)
            t = StudentUtil.cursor.fetchone()            
            if t:
                if 'name' in kwargs and 'addr' not in kwargs :                    
                    query = "update studenttb set sname='{}' where id={}".format(kwargs["name"],id)
                elif 'addr' in kwargs and 'sclass' not in kwargs:
                    query = "update studenttb set saddr='{}' where id={}".format(kwargs["addr"],id)
                elif 'sclass' in kwargs and 'name' not in kwargs:
                    query = "update studenttb set sclass='{}' where id={}".format(kwargs["sclass"],id)
                else:
                    query = "update studenttb set sname = '{}' ,saddr = '{}' ,sclass='{}' where id={}".format(kwargs["name"],kwargs["addr"],kwargs["sclass"],id)
                StudentUtil.cursor.execute(query)
                StudentUtil.conn.commit()
                return "Succefully updated"
            else:
                return "Record not found"   
        except mysql.connector.Error as msg:
            print(msg)
    @staticmethod
    def Savestudent(std):
        try:
            query = "INSERT INTO STUDENTTB(sname,saddr,sclass) VALUES ('{}','{}','{}')".format(std.sname,std.saddr,std.sclass)
            StudentUtil.cursor.execute(query)
            StudentUtil.conn.commit()
            return "Succeessfully inserted"
        except mysql.connector.Error as msg:
            return msg 
    @staticmethod
    def deletestd(id):
        try:
            query = "DELETE FROM STUDENTTB WHERE ID = {}".format(id)
            StudentUtil.cursor.execute(query)
            StudentUtil.conn.commit()
            return "Succeessfully deleted"
        except mysql.connector.Error as msg:
            return msg 
    @staticmethod
    def showallstd():
        try:
            query = "SELECT * FROM STUDENTTB "
            StudentUtil.cursor.execute(query)
            m = StudentUtil.cursor.fetchall()
            print("{:<5}{:10}{:10}{:10}".format("ID","NAME","ADDR","CLASS"))
            for t in m:
                print("{:<5}{:10}{:10}{:10}".format(t[0],t[1],t[2],t[3]))
                #print('',t[0],'\t',t[1],'\t',t[2],'\t',t[3])
            StudentUtil.conn.commit()
            return "Succeessfully Shown All Student"
        except mysql.connector.Error as msg:
            return msg 
    @staticmethod
    def searchstdby(**kwargs):
        try:
            if 'sid' in kwargs:
                query = "SELECT * FROM STUDENTTB WHERE ID LIKE '{}%'".format(kwargs["sid"])
            elif 'sname' in kwargs:
                query = "SELECT * FROM STUDENTTB WHERE SNAME LIKE '{}%'".format(kwargs["sname"])
            elif 'saddr' in kwargs:
                query = "SELECT * FROM STUDENTTB WHERE SADDR LIKE '{}%'".format(kwargs["saddr"])
            elif 'sclass' in kwargs:
                query = "SELECT * FROM STUDENTTB WHERE SCLASS LIKE '{}%'".format(kwargs["sclass"])
            StudentUtil.cursor.execute(query)
            m = StudentUtil.cursor.fetchall()
            print(" ID\t NAME\t ADDR\t CLASS\t")
            for t in m:
                print('',t[0],'\t',t[1],'\t',t[2],'\t',t[3])
            StudentUtil.conn.commit()
        except mysql.connector.Error as msg:
            return msg 