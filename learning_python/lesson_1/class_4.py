class Person():

  def __init__(self, name, jobs, age =None):
      self.name= name
      self.jobs=jobs
      self.age = age
  def info(self):
      return (self.name, self.jobs)

per1 =Person('Shivika', ['mgr', 'ceo'], 45)
per2 =Person('Arvind', ['sen mgr', 'dir'])

print(per1.jobs)
print(per2.info())

