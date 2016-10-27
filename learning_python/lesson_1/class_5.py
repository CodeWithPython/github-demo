class Person():
    def __init__ (self, name, job =None, pay =0):
       self.name = name
       self.job = job
       self.pay = pay
   
    def lastname(self):
       return self.name.split()[-1]

    def giveRaise(self, percent):
       self.pay = int(self.pay*(1+percent))
       return self.pay
   
    def __repr__(self):
       return '[Person: %s, %s]' % (self.name, self.pay)
  

if __name__ == '__main__':
   in1 = Person('Shivika Jindal', pay = 20000)
   in2= Person('Simson Bold', job ='mgr', pay =10000)
   print in1
   print (in1.name, in1.pay, in1.job)
   print (in2.name, in2.pay, in2.job)
   print(in2.name.split()[-1])
   in2.pay *=1.10
   print('%.2f' % in2.pay)
   in3 = Person('Arvind Varadarajan', job ='dir', pay =30000)
   print(in3.lastname())
   print(in3.giveRaise(.20))








