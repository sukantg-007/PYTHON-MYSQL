class Student:
    def __init__(self,sname,saddr,sclass):
        self.sname = sname
        self.saddr = saddr
        self.sclass = sclass
    def __str__(self):
        return "Name :{}\tAddr :{}\tClass :{}".format(self.sname,self.saddr,self.sclass)
