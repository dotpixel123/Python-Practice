# n = int (input("Enter your number here "))
# for i in reversed (range(1,11)):
#     print (str(n) + " times " + str(i) + " are " + str(n*i))
    # print (f" {n} times {i} is equal to {n*i}") 

# l1 = ['Harry', 'Soham', 'Sachin', 'Rahul']
# for item in l1 :
#     if item.startswith("S"):
#         print ('Good morning',item )

# n = int (input("Enter your number here "))
# i = 0
# while i <= 10 :
#     print (f"{n} times {i} is {n*i}")
#     i = i+1 

n = int (input('Enter your number here ')) 
prime= True
for i in range(2,n):
    if n%i == 0 :
        prime = False
        break
if prime :
    print ('yes')
else :
    print ('no')

# n = int (input("Your number here "))
# for n in range (1,n+1):
#     print (n * "*")
