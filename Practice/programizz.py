# # Problem 3
# a = float(input('Enter a number here: \n'))
# b = a**(1/2) 
# print(b)

# # This program adds two numbers

# num1 = 1.5
# num2 = 6.3

# # Add two numbers
# sum = num1 + num2

# # Display the sum
# print('The sum of {} and {} is {}'.format(num1, num2, sum))


# # Problem 4 
# b = int(input('Enter the base of triangle \n'))
# h = int(input('Enter the height of the triangle \n'))
# area = (1/2)*b*h
# print(area)

# # Problem 5 
# a = int(input('Enter coefficient of x^2\n'))
# b = int(input('Enter coefficient of x\n'))
# c = int(input('Enter the constant\n'))
# D = ( b**2 - 4*a*c )**(1/2) 
# x1 = (-b - D)/2 
# x2 = (-b + D)/2
# print(f'The roots of equation are {x1} and {x2}') 

# # Problem 6 
# x = 'some variable'
# y = 'which I want to swap'
# z = x 
# x = y 
# y = z 
# print(x)
# print(y)

# # Problem 7
# import random 
# pick = random.randrange(1000)
# print(pick)

# # Problem 8 
# km = float(input('Enter the distance in km \n'))
# miles = 0.621371 *km 
# print(miles)

# # Problem 10 
# a = int(input('Enter a number here\n'))
# if a == 0 : 
#     print('Your number is equal to 0')
# if a < 0 : 
#     print('Your number is smaller than 0')
# if a > 0 : 
#     print('Your number is greater than 0 ')

# # Problem 11 
# a = int(input('Enter a number here \n'))
# if a%2 == 0 : 
#     print('Your number is even')
# else : 
#     print('It is odd')

# # Problem 13
# a = float(input('Enter number here \n'))
# b = float(input('Enter number here \n'))
# c = float(input('Enter number here \n'))
# print(max(a,b,c))

# # Problem 14 
# a = int(input('Enter your number here \n'))
# for n in range(2,a):
#     if a % n == 0 :
#         print(f'{a} is not a prime number')
# else : 
#     print(f'{a} is a prime number')

# # Problem 15 
# n = int(input('Enter the range here \n'))
# for i in range (2,n): 
#     prime = False
#     for j in range (2,i):
#         if i%j != 0:
#             prime = True
#     if prime == True: 
#         print(i)x
#     else : 
#         print('okay')

# # Problem 16 
# n = int(input('Enter a number:\n'))
# fact = 1
# for i in range(n): 
#     fact = fact * (n-i)
# print(fact)

# # Problem 18
# list = [0,1] 
# for i in range(15): 
#     sum_of_last = 0
#     elements = 0
#     list.reverse()
#     while elements < 2:
#         sum_of_last = sum_of_last + list[elements]
#         elements = elements + 1 
#     list.reverse()
#     list.append(sum_of_last)
# print(list)

# # Method 2 
# list = [0,1]
# for i in range(15): 
#     list.append(sum(list[-2:]))
# print(list)

# # Problem 19 
# n = str(input('Enter a number here \n'))
# sum_of_cube = 0 
# for i in range(len(n)): 
#     sum_of_cube = sum_of_cube + (int(n[i]))**int(len(n))
# if sum_of_cube == int(n) : 
#     print('yes')
# else : 
#     print('no')

# # Problem 20 
# for i in range(1000):
#     i = str(i)
#     sum_of_cube = 0
#     for digits in range(len(str(i))):
#         sum_of_cube = sum_of_cube + (int(i[digits]))**int(len(i))
#     if sum_of_cube == int(i): 
#         print(i)

# # # Problem 21 
# def recur_sum(n):
#    if n <= 1:
#        return n
#    else:
#        return n + recur_sum(n-1)
# print(recur_sum(10))

# # Problem 39
# string = input('Enter a string here\n')
# mylist = []
# for i in string: 
#     mylist.append(i)
# print(mylist)

# if mylist == reversed(mylist): 
#     print('The string is a palidrome!!') 
# else: 
#     print('It is not a palindrome')

