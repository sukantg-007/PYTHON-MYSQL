class Student:
    def __init__(self,id,sname,saddr,sclass):
        self.id = id
        self.sname = sname
        self.saddr = saddr
        self.sclass = sclass
    def __str__(self):
        return "Id : {}\tName :{}\tAddr :{}\tClass :{}".format(self.id,self.sname,self.saddr,self.sclass)
