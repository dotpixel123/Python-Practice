# # Animation in python
# for n in range(100000000):  
#     if n%1000000 == 0 : 
#         i = int(n/1000000) 
#         if i%2 != 0: 
#             print('        ')
#             print('┗( ･o･)┓')
#             print('        ')
#             print('  O    ')
#             print(' /|\    ')
#             print(' / \    ')
#         else : 
#             print('        ')
#             print('┏(・o･)┛')
#             print('        ')
#             print('  O    ')
#             print('  |\\\  ')
#             print('  /\    ')
            

# print('')
# print(' ___     ~~  ~~ ')
# print('/__/|           ')
# print('|  ||     .     ')
# print('|  ||    /|\    ')
# print('|__|/    / \    ')

## To find the area of circle 
# r = float(input("Select the radius\n"))
# a = (3.1415926535)*(r)**2 
# print (a)

## Power table 
# def power_table(a):
#     for i in range (10):
#         print (a**i)
# (power_table(54))        

## Print username in reversed order
# a = input("Enter your firstname here\n")
# b = input('Enter your last name here\n')
# print (b + ' ' + a)

## To print user given numbers in a list and a tuple 
# num = input('enter your numbers here\n')
# l = num.split(',')
# print (l)
# print (tuple(l))

## To check if a number is odd or even 
# num = int(input("Enter your number here \n"))
# if num % 2 == 0 :
#     print ('The number you have chosen is even ')
# else :
#     print ('The number you have chosen is odd ')

# def times_print(a):
#    for i in range (1,n+1):
#       print (a)

# exam_st_date = (11, 12, 2014)
# print('The exam will start from :',exam_st_date[0],'/',exam_st_date[1],'/',exam_st_date[2])
# print('The exam with start from : %s/%s/%s'%(exam_st_date))

# n1 = int(input('Enter your number here \n'))
# n2 = int(input('Enter your number here \n'))
# n3 = int(input('Enter your number here \n'))
# def sum (a,b,c):
#     if a != b != c:
#         return a + b + c
#     elif a ==b ==c :
#         return 3*(a + b + c)
# print(sum(n1,n2,n3))

# string = str(input('Enter a statement\n'))
# if string.startswith("Is") == True :
#     print(string)
# elif string.startswith('Is') == False:
#     print(f'If {string}')

# n = int(input('Enter amount of times to print\n'))
# str = str(input('Enter a string to be printed n number of times\n'))
# if len(str)>2:
#     print (n*(str[0:2]))
# else :
#     print (n*str)

# tuple = (13,1,321,13,1,3,43,143)
# n = int(input('Ask for a number in the tuple \n'))
# if n in tuple :
#     print ('Yes')
# else :
#     print('No')

# str = str(input('Enter anything \n'))
# def histogram (a,b,c,d):
#     list = [a,b,c,d]
#     for i in range (len(list)):
#         print (list[i]*str)
# histogram(2,4,5,1)

## To print all prime number between 0 to n
# a = int(input('Enter a number \n'))
# b = int(input('Enter a number \n'))
# def all_prime (a,b):
#     # loop to check for all numbers till a 
#     for i in range(3,b):
#         # dividing each i by every number j to check for prime
#         for j in range (2,i):
#             if i%j == 0 :
#                 break 
#         else :
#             print(i)
# all_prime(a,b)

# # To print prime factors of a number
# def prime_factor(a):
#     for i in range(2,a+1): 
#         if a%i == 0 :
#             x = a/i 
#             print(i) 
#             return prime_factor(int(x))
# n = int(input('Enter a number \n'))
# prime_factor(n)

# # To print LCM of 2 numbers (1st method)
# a = int(input('Enter first number\n'))
# b = int(input('Enter second number\n'))
# def lcm(a,b):
#     for i in range (1,(a*b)+1):
#         if i%a == i%b == 0 :
#             print (i)
#             break 
# lcm(a,b)

## (2nd method)
# def lcm(x, y):
#   if x > y:
#       z = x
#   else:
#       z = y
#   while(True):
#       if((z % x == 0) and (z % y == 0)):
#           lcm = z
#           break
#       z = z+1
#   return lcm
# print(lcm(4, 6))
# print(lcm(15, 17))

# # To print HCF of 2 numbers 
# a = int(input('Enter first number\n'))
# b = int(input('Enter second number\n'))
# def hcf(a,b):
#     for i in reversed(range(b+1)):
#         if b%i == a%i == 0 :
#             print(i)
#             break 
# hcf (a,b)

# def simple_interest(p,r,t):
#     total_amount = (p*r*t/100) + p 
#     return total_amount 
# print(simple_interest(10000,3.5,7))

# import multiprocessing
# print(multiprocessing.cpu_count())

## Hide credit card number (1st method)
# n = str(input('Enter your credit card number here: \n'))
# print((len(n)-4)*'*'+n[-4:])

## 2nd method
# n = str(input('Enter your credit card number here: \n'))
# i = 0 
# while i <= len(n) :
#     i += 1 
#     if i <= len(n)-4:
#         print ('*', end = '')
# print(n[-4:])

## To remove strings from a list and print only numbers 

# list = [9,248294,9,9]
# def array_front9(nums):
#     for num in nums :
#         print(num)
#         if num == 9 :
#             return True 
#         else :
#             return False
# print(array_front9(list))

# # Shuffling a deck of cards
# list = []
# for n in range(3,7):
#         for i in range (1,11):
#                 list.append(f'{i} of {chr(n)}')
#         for k in 'Jack','Queen','King':
#                 list.append(f'{k} of {chr(n)}')
# import random
# random.shuffle(list)
# for elements in list : 
#         print (elements)

# string = str(input('Enter a string \n'))
# vowels = 0 
# for i in string :
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         vowels=vowels+1 
# print(vowels)
# print('hi')

# # Solving quadratic equations 
# a = int(input('Enter coefficient of x^2 \n'))
# b = int(input('Enter the coefficient of x \n'))
# c = int(input('Enter the constant \n'))
# def sign (a):
#     if a < 0 :
#         sign1 = '-'
#     else :
#         sign1 = '+'
#     return (sign1)
# print(f'Solving {sign(a)} {abs(a)}x^2 {sign(b)} {abs(b)}x {sign(c)} {abs(c)} ..........')
# def solve_qe(a,b,c):
#     import cmath 
#     d = cmath.sqrt((b**2)-4*a*c)
#     root1 = (-b - d)/(2*a)
#     root2 = (-b + d)/(2*a) 
#     return f'The roots of the equation are \n a = {root1} \n b = {root2} '
# print(solve_qe(a,b,c))

# import calendar
# yy = 6969
# mm = 5
# dd = 7 
# print(calendar.month(yy,mm))

## Check for panlindrome 
# string = str(input('Enter a phrase\n')) 
# string1 = string.replace(' ','')
# list1 = []
# for i in string1 :
#     list1.append(i) 
# list2 = []
# for i in reversed(string1) :
#     list2.append(i)
# if list1 == list2 :
#     print ('The string is a palindrome')
# else :
#     print ('The string is not a palindrome')

# # Making a matrix
# order_rows = int(input('How many rows of matrix you want '))
# order_column = int(input('How many columns of matrix you want '))
# matrix = []
# for rows in range(order_rows): 
#     elements = input(f'Enter {rows+1} row elements\n')
#     if len (elements.split(',')) != order_column :
#         print('Number of elements should be according to order of matrix!! ')
#         break 
#     else :
#         elements = elements.split(',')
#         matrix.append(elements)
# for element in matrix: 
#         print(element)

## Add matrix(1st attempt)
# matrix_1 = [[1,6,3],
#             [4,8,21],
#             [6,2,4]]
# matrix_2 = [[12,7,3],
#             [4,5,6],
#             [7,8,9]]
# result_matrix = [[0,0,0],
#                  [0,0,0],
#                  [0,0,0]]  
# for row in range(len(matrix_1)):
#     for i in range(len(matrix_1[0])):
#         result_matrix[row][i] = matrix_1[row][i] + matrix_2[row][i]
# for i in result_matrix:
#     print(i)


        # result_matrix.append(matrix_1[row][elements]+ matrix_2[row][elements])

# list1 = [23,1,31,32,2]
# list2 = [315,351,4,7,28]
# for i in range(len(list1)):
#     print(list1[i]+ list2[i])

## Program to add two matrices using nested loop (solution)
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
# # iterate through rows
# for i in range(len(X)):
#    # iterate through columns
#    for j in range(len(X[0])):
#        result[i][j] = X[i][j] + Y[i][j]
# for r in result:
#    print(r)

# # Tranpose of a matrix
# matrix_1 = [[1,6,3],
#             [4,8,21],
#             [6,2,4]]
# transpose = [[0,0,0],
#             [0,0,0],
#             [0,0,0]]
# for i in range(len(matrix_1)): 
#     for j in range(len(matrix_1[0])):
#         transpose[i][j] = matrix_1[j][i]
# for t in transpose: 
#     print(t)

# # Sasta Multiplication of matrix 
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
# result_matrix = [[0,0,0],
#                 [0,0,0],
#                 [0,0,0]]
# for row in range(len(X)) :
#     for elements in range(len(X[0])):
#         result_matrix[row][elements] =  (X[row][elements])*(Y[row][elements])
# for elements in result_matrix:
#     print(elements)

# # Real Multiplication of 2 matrices 
# X = [[12,7,3,4,5],
#     [4,5,6,3,3],
#     [7,8,9,0,9]]
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9],
#     [4,3,2],
#     [8,7,1]]
# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
# if len(X[0]) == len(Y):
#         for rows in range(len(X)): 
#                 for elements in range(len(X)):
#                         temp_list = []
#                         for columns in range(len(Y)):
#                                 n = int(X[rows][columns]*Y[columns][elements])
#                                 temp_list.append(n)
#                         result[rows][elements] = sum(temp_list)

# else : 
#         print('The number of columns in the first matrix must be equal to the number of rows in the second matrix!!')
# for i in result: 
#         print(i)

# # Maximum and minimum value of user numbers
# list = []
# while True:
#     user_input = input('Enter integers here or done to stop\n')
#     try: 
#         user_input = int(user_input)
#     except: 
#         if user_input == 'done': 
#             break 
#         else: 
#             print('Invalid input')
#             continue
#     list.append(user_input)
# print('Maximum is '+ str(max(list)))
# print('Minimum is '+ str(min(list)))

# string = 'This course can give me a big hand for my future studies I have seen many positive reviews about this course so I want to complete this course for enhancing my knowledge and showing this certificate for my future university .... I  plan to get into a good university and they say that this course can give an edge to my performance soo it is worth it and also this course will help me in getting a good job and pay the loans as I mentioned earlier there is an amount of loan to clear so I need to earn money in future and  this is the best possible option so I request you to accept the financial aid and I promise that I will complete this course on time as I have finished previous 2 courses and I am serious about my future so please accept my financial aid it will be very helpful for me'
# word_count = 0 
# for i in string: 
#     if i == ' ': 
#         word_count = word_count + 1 
#     else: 
#         continue
# print(word_count)

# # Capital indexes
# def capital_indexes(string): 
#     pos = -1
#     mylist = []
#     for letter in string: 
#         pos += 1
#         if letter.isupper() is True : 
#             mylist.append(pos)
#         else: 
#             continue
#     print(mylist)
# capital_indexes('TEsT')

# # Online status
# statuses = {
#     "Alice": "online",
#     "Bob": "offline",
#     "Eve": "online",
# }
# def online_count(mydict):
#     online_count = 0  
#     for i in mydict: 
#         if mydict.get(i) == 'online': 
#             online_count += 1 
#         else: 
#             continue
#     return online_count
# print(online_count(statuses))

# # PRINTING COMMAS BETWEEN NUMBERS
# # Method 1
# import math
# def format_number(num): 
#     if num > 0: 
#         num = list(str(num))
#         num.reverse()
#         l = math.ceil(len(num)/3)
#         for i in range(0,l): 
#             num.insert(4*i,',')
#         num.pop(0)
#         num.reverse()
        # return ''.join(num)
# # Method 2
# def format_number(n):
#     return "{:,}".format(n)
# print(format_number(100000010000)) 

# # Function with variable amount of arguments
# def function(*arg): 
#     return len(arg)
# print(function(1,3,4,5,3))

# # LIST XOR
# # Method 1
# def list_xor(n,mylist1,mylist2): 
#     if n not in mylist1 and n not in mylist2: 
#         return False
#     elif n not in mylist1 or n not in mylist2: 
#         return True
#     else: 
#         return False
# # Method 2 
# def list_xor(n, list1, list2):
#     return (n in list1) ^ (n in list2)
# print(list_xor(4,[3,4,32,2],[4,15,43]))

def validate(validate): 
    if 'def' not in validate: 
        return 'missing def'
    elif ':' not in validate: 
        return 'missing :'
    elif '()' in validate: 
        return 'missing param'
    elif '    ' not in validate: 
        return 'missing indent'
    elif 'validate' not in validate: 
        return 'wrong name'
    elif 'return' not in validate: 
        return 'missing return'
    else: 
        return True
string = ''' def validate(validate): 
    if 'def' not in validate: 
        return 'missing def'
    elif ':' not in validate: 
        return 'missing :'
    elif '()' in validate: 
        return 'missing param'
    elif '    ' not in validate: 
        return 'missing indent'
    elif 'validate' not in validate: 
        return 'wrong name'
    elif 'return' not in validate: 
        return 'missing return'
    else: 
        return True '''
# print(validate(string))

# mydict = {}
# mystr = input('Enter the word or string here\n')
# for i in mystr: 
#     mydict[i] = mydict.get(i,0) + 1
# for k,v in mydict.items(): 
#     print(k,v)

n = input('Enter a number ')
l = n.split('')
print(l)
