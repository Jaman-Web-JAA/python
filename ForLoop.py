# for i in "apple":
#     print(i)
#------------------
# for i in range(5):
#     print(i)

#-------------------
# for i in range(1,5):
#     print(i)
#-------------------
# for i in range(1,11):
#     print(i,"* 2 =",i*2)
#-------------------
# a = int(input())
# b = int(input())
# for a in range(a+1,b):
#     print(a)

#--------------------
# for i in range(1,11):
#     if(i%2==0):
#         print("The even number is :", i)
#-------------------
# count = 0
# for i in range(1,11):
#     if(i%2==0):
#         count=count+1
# print("The count of even numbers :", count)
#----------------------

# count_odd = 0
# count_even = 0
# for i in range(1,11):
#     if(i%2==0):
#         count_even=count_even+1
#     else:
#         count_odd=count_odd+1
# print("odd: ",count_odd)
# print("even: ",count_even)

#--------------------
# count=0
# for i in range(1,101):
#     if(i%3 == 0 and i%5 ==0):
#         count=count+1
# print(count)

#---------------------
# sum=0
# for i in range(1,6):
#     sum = sum+i
# print(sum)
#--------------------
# a=[1,2,3,4,5]
# for i in a:
#     print(i)
#-------------------
a=[]
print("Enter 10 Number: ")
for i in range(5):
    num=int(input("Enter num " + str(i+1)+": "))
    a.append(num)
print(a)
sum=0
for i in a:
    sum=sum+i
avg = sum/len(a)
print(sum)
print(avg)