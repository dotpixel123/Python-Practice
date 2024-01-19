# Try and exception 
# a = input('Enter a number here \n')
# try:
#     a = int(a)
#     print(1/a)
# except Exception as e :
#     print(e) # prints the exception
#     print('That is not a number.')

# # Different types of errors and else and finally
# a = input('Enter a number here \n')
# try:
#     a = int(a)
#     print(1/a)
# except ValueError as e :
#     print(e) 
#     print('That is not a number.')
#     quit()
# except ZeroDivisionError as e:
#     print(e) 
#     print('Cannot divide by 0')
# else: 
#     print('You entered the right number') # Only runs when try is successful
# finally: 
#     print('This lines prints regardless even if exception occured')

# # How to raise your own error
# a = input('Enter a number here \n')
# try:
#     a = int(a)
#     print(1/a)
# except ValueError as e :
#     print(e) 
#     print('That is not a number.')
# except:
#     raise ZeroDivisionError('Cannot divide by 0')

# # Global and local variable
# a = 5
# def func1(): 
#     a = 4 # local variable
#     return a
# def func2(): 
#     global a # makes changes to the global variable
#     a = 4
#     return a
# print(a)
# print(func1())
# print(a)
# print(func2())
# print(a)

# # Enumerate 
# myList = [3,51,'5,1.6m,',153,'m16',0.16,True]
# for index, item in enumerate(myList):
#     print(item,index)

# # List comprehension 
# myList2 = [3,13,61,16,464,1]
# req_list = []
# for element in myList2:
#     if element < 15: 
#         req_list.append(element)
# print(req_list)
#         # OR 
# req_list2 = [element for element in myList2 if element < 15]
# print(req_list2)

# # Lambda functions
# def func(x):
#     x += 5
#     return x 
# num = 555
# print(func(num))
#         # OR
# func = lambda x : x+5
# num = 655
# print(func(num))

# # .join function 
# friends = ['Shubham','Shourya','Shreshth']
# string = ' and '.join(friends)
# print(string) 

# # .format 
# name = 'Shourya'
# age = 17
# hobby = 'drawing'
# string = 'My name is {} and my age is {}. Also I love {}'.format(name, age, hobby)
# string2 = 'My hobby is {2}. My name is {0}. My age is {1}'.format(name, age, hobby)
# print(string)
# print(string2)

# Map
square = lambda x : x**2
myList = [1,3,4]
l2 = []
for i in myList: 
    l2.append(square(i))
print(l2)
        # OR
square = lambda x : x**2
print(list(map(square,myList)))

# Filter
greater_than_10 = lambda x : x > 10
myList = [4,426,6,27,2,472,72,54,541,36,27,5,57]
print(list(filter(greater_than_10,myList)))