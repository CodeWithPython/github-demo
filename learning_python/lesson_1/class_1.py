class FirstClass:
   def setData(self, value):
      self.data= value
  
   def display(self):
      print("The value is "+ str(self.data))

x = FirstClass()
y = FirstClass()

x.setData("Shivika")
x.display()
y.setData(12345)
y.display()

class SecondClass(FirstClass):
   def display(self):
     print("Current Value is %s" % self.data)
 
z =SecondClass()
z.setData(42)
z.display()
x.setData(89)
x.display()

