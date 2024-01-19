# # 1st method
# class programmer: 
#     company = 'Microsoft'
#     def details(self): 
#         print(f'{self.name} works in {self.company} and is {self.age} year old')
# shourya = programmer()
# shourya.name = 'Shourya'
# shourya.age = 32
# shubham = programmer()
# shubham.name = 'Shubham'
# shubham.age = 29
# shourya.details()
# shubham.details()
# # 2nd method
# class programmer: 
#     company = 'Microsoft'
#     def __init__(self,name,age): 
#         self.age = age
#         self.name = name
#     def details(self): 
#         print(f'{self.name} works in {self.company} and is {self.age} year old')
# shourya = programmer('Shourya',32)
# shubham = programmer('Shubham',29)
# shourya.details()
# shubham.details()

# class calculator: 
#     def __init__(self,val):
#         self.val = val
#     def square(self): 
#         print(f'The square of {self.val} is {self.val**2}')
#     def cube(self): 
#         print(f'The cube of {self.val} is {self.val**3}')
#     def square_root(self): 
#         print(f'The value of square root of {self.val} is {self.val**(1/2)}')
# first_num = int(input('Enter the num here\n')) 
# num = calculator(first_num)
# num.square()
# num.cube()
# num.square_root()

# class sample: 
#     a = 'class attribute'
# something = sample()
# print(something.a)
# something.a = 'object attribute now'
# print(something.a)

class calculator: 
    @staticmethod
    def greet(): 
        print('Hello user')
    def __init__(self,val):
        self.val = val
    def square(self): 
        print(f'The square of {self.val} is {self.val**2}')
    def cube(self): 
        print(f'The cube of {self.val} is {self.val**3}')
    def square_root(self): 
        print(f'The value of square root of {self.val} is {self.val**(1/2)}')
first_num = int(input('Enter the num here\n')) 
num = calculator(first_num)
num.greet()
num.square()
num.cube()
num.square_root()
