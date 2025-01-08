#while loop is usually used when the number of iterations is unknown.

# i=1
# while(i<=5):
#     print(i)
#     i=i+1
#----------------
# i=1
# while(i<=20):
#     print(i*10)
#     i=i+1

#-----------------
# i=10
# while(i>0):
#     print(i,end=",")
#     i=i-1
#--------------------


#factorial

i=3
fact=1
while(i>0):
    print(i,end=",")
    fact=fact*i
    i=i-1
print()
print(fact)
