from class_1 import FirstClass
class ThirdClass(FirstClass):
   def display(self):
     print("Now the value is %s" % self.data)

m = ThirdClass()
m.setData(34)
m.display()

