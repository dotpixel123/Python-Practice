# file_name = input('Enter the file name here -\n')
# mode = input('Read, write or append?\n')
# try:
#     with open(file_name,mode) as file:
#         data = file.read()
# except Exception as e: 
#     print(e)
#     print('There is no file found by such name.')

user = int(input('Enter a number here: \n'))
mul_list = [f'{user} times {j} is {user*j}' for j in range(10)]
print(mul_list)