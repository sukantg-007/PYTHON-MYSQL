from StudentUtilModule import StudentUtil
from studentinfo import Student
while True:
    print("****MENU*****")
    print("1. ADD STUDENT")
    print("2. UPDATE STUDENT")
    print("3. DELETE STUDENT")
    print("4. SEARCH STUDENT")
    print("5. SHOW ALL STUDENTS")    
    print("6. EXIT")    
    choice=int(input("Enter ur choice : "))
    if choice==1:
        print("Enter student info")
        name=input("NAME  : ")
        addr=input("ADDR  : ")
        sclass=input("CLASS : ")
        s=Student(name.upper(),addr.upper(),sclass.upper())
        print(s)
        msg=StudentUtil.Savestudent(s)
        print(msg)
    elif choice==2:
            print("Update Info")
            print("1. UPDATE NAME")
            print("2. UPDATE ADDR")
            print("3. DELETE CLASS")
            print("4. UPDATE NAME,ADDR,CLASS")    
            choice2 = int(input("Enter ur choice : "))
            id = input("Enter Student Id: ")
            if choice2 == 1:
                new_name = input("Enter name to update :")
                msg = StudentUtil.stdupdate(id,name=new_name.upper())
                print(msg)
            elif choice2 == 2:
                new_addr = input("Enter addr to update :")
                msg = StudentUtil.stdupdate(id,addr=new_addr.upper())
                print(msg)
            elif choice2 == 3:
                new_class = input("Enter class to update :")
                msg = StudentUtil.stdupdate(id,sclass=new_class.upper())
                print(msg)
            elif choice2 == 4:
                new_name = input("Enter name to update :")
                new_addr = input("Enter address to update :")
                new_class = input("Enter class to update :")
                msg = StudentUtil.stdupdate(id,name=new_name.upper(),addr=new_addr.upper(),sclass=new_class.upper())
                print(msg)
            else :
                print("Invalid Input")
    elif choice==3:
        id = input("Enter Student Id: ")
        msg = StudentUtil.deletestd(id)
        print(msg)
    elif choice==4:
        print("1. Search By ID")
        print("2. Search By Name")
        print("3. Search By Address")
        print("4. Search By Class")
        choice3 = input("Enter Search Option")
        if choice3 == '1':
            id = input("Enter your id : ")
            msg = StudentUtil.searchstdby(sid = id)
            print(msg)
        elif choice3 == '2':
            name = input("Enter your name : ")
            msg = StudentUtil.searchstdby(sname = name)
            print(msg)
        elif choice3 == '3':
            addr = input("Enter your addr : ")
            msg = StudentUtil.searchstdby(saddr = addr)
            print(msg)
        elif choice3 == '4':
            stclass = input("Enter your class : ")
            msg = StudentUtil.searchstdby(sclass = stclass)
            print(msg)
        else:
            print("INVALID INPUT!")
    elif choice==5:
        msg = StudentUtil.showallstd()
        print(msg)    
    elif choice==6:
        print("Good bye...")     
        break
    else:
        print("Invalid Input")