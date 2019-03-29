class rectangle:
     def __init__(self,len=0,brth=0):
         self.len=len
         self.brth=brth
     def calArea(self,rc):
         area=rc.len*rc.brth
         print("area: ",area)

length=int(input("enter the value of length :"))
breadth=int(input("enter the value of breadth:"))
a=rectangle(length,breadth)
b=rectangle()
b.calArea(a)
