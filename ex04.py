from StudentUtilModule import StudentUtil
from studentinfo import Student

while True:
    print("****MENU*****")
    print("1. ADD STUDENT")
    print("2. UPDATE STUDENT")
    print("3. DELETE STUDENT")
    print("4. SHOW STUDENT")
    print("5. SHOW ALL STUDENTS")    
    print("6. EXIT")    
    choice=int(input("Enter ur choice : "))
    if choice==1:
        #save student
        print("Enter student info")
        id=input("ID    : ")
        name=input("NAME  : ")
        addr=input("ADDR  : ")
        sclass=input("CLASS : ")
        s=Student(id,name,addr,sclass)
        print(s)
        msg=StudentUtil.Savestudent(s)
        print(msg)
    elif choice==2:
        #update student
        pass
    elif choice==3:
        #delete student
        pass
    elif choice==4:
        #show particular student
        pass
    elif choice==5:
        #show all student
        pass
    elif choice==6:
        print("Good bye...")     
        break
    else:
        #show error msg
        pass
        
