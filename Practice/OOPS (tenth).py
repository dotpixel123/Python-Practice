class form: 
    formtype = 'application'
    def printdata(self): 
        print('name is', self.name)
myapplication = form() 
myapplication.name = 'Shourya'
myapplication.printdata()

class employee: 
    company = 'Google'
    salary = '30k'
person1 = employee()
print(person1.company)
print(person1.salary)
person1.salary = '40k'
print(person1.salary)

class employee: 
    company = 'Google'
    salary = '30k'
    def details(self): 
        print(f'{self.name} works in {self.company} and his salary is {self.salary} ')
worker = employee()
worker.name = 'Shourya'
worker.details() # OR
employee.details(worker) # Both are same 

class employee: 
    company = 'Google'
    salary = '30k'
    def __init__(self,name,age): # Constructor
        self.name = name
        self.age = age 
    def details(self): 
        print(f'{self.name} is {self.age} years old and works in {self.company} and his salary is {self.salary} ')
worker = employee('Shourya',30)
worker.details()