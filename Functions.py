# def painter():
#     print("Painting")
    
# painter()

# ------------
# def add(a,b):
#     c = a+b
#     print(c)
# def sub(a,b):
#     c = a-b
#     print(c)
# def mul(a,b):
#     c = a*b
#     print(c)
# def div(a,b):
#     c = a/b 
#     print(c)

# a = int(input("Enter a value : "))
# b = int(input("Enter b value : "))
# add(a,b)
# sub(a,b)
# mul(a,b)
# div(a,b)

# ------------
# def oddoreven(a):
#     if(a%2==0):
#         print("given number is even number")
#     else:
#         print("given number is odd number")

# a = int(input("enter the number: "))
# oddoreven(a)

#--------------------

# def passfail(a):
#     if(a>=35):
#         print("Pass")
#     else:
#         print("fail")

# a = int(input("enter the mark: "))
# passfail(a)

#--------------------

def printrange(a,b):
    for i in range(a,b):
        print(i)

a = int(input("enter the a value: "))
b = int(input("enter the b value: "))
printrange(a,b)