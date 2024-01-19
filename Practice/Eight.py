# def greet(name = "Stranger") :
#     return "Have a good day " + name  
# print (greet("Shourya")) 
# print (greet ())

n= int(input("Enter your numbere here \n"))
def factorial(n) :
    product = 1
    for i in range (n):
        product = product * (i+1)
    return product 
print (factorial(n))

# n= int(input("Enter your numbere here \n"))
# def factorial2(n):
#     if n == 1 or n == 0 :
#         return 1
#     return n * factorial2(n-1)
# print (factorial2(n))