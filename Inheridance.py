# class dad():
#     def phone(self):
#         print("Dad's phone")

# class son():
#     def laptop(self):
#         print("Son's laptop")

# ram = son()
# ram.phone()

# ------------------
# single inheritance
# class dad():
#     def phone(self):
#         print("Dad's phone")

# class son(dad):
#     def laptop(self):
#         print("Son's laptop")

# ram = son()
# ram.phone()

# ---------------------
# multiple inheridance
# class dad():
#     def phone(self):
#         print("Dad's phone")

# class mom():
#     def sweet(self):
#         print("Mom's sweet")

# class son(dad,mom):
#     def laptop(self):
#         print("Son's laptop")

# ram = son()
# ram.phone()
# ram.sweet()
# ---------------------
# multilevel inheridance
# class grandpa():
#     def phone(self):
#         print("Grandpa's phone")

# class dad(grandpa):
#     def money(self):
#         print("Dad's money")

# class son(dad):
#     def laptop(self):
#         print("Son's laptop")

# ram = son()
# ram.laptop()
# ram.money()

# d1=dad()
# d1.phone()

# -------------------------
# Hierarchical inheridance
# class dad():
#     def money(self):
#         print("Dad's money")

# class son1(dad):
#     pass
# class son2(dad):
#     pass
# class son3(dad):
#     pass

# s2=son2()
# s2.money()

# ---------------------
# hybrid inheridance
# class dad():
#     def money(self):
#         print("dad money")

# class land():
#     def important(self):
#         print("important land")
        
# class son1(dad,land):
#     pass
# class son2(dad):
#     pass
# class son3(dad):
#     pass

# s1=son1()
# # s1.money()
# s1.land()

# -------------------
# hybrid inheridance
class School:
    def func1(self):
        print("This function is in school.")
 
 
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
 
 
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
 
 
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")
 
 
# Driver's code
object = Student3()
object.func1()
object.func2()