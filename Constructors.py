# Constructor is a unique function that gets called automatically when an object is created of a class.
# The main purpose of a constructor is to initialize or assign values to the data members of that class.
# self keyword - it is used to denote current object.

# class Laptop():
#     def display(self):
#         print("Display")

# hp = Laptop()
# hp.display()
# ------------

# class Laptop():
#     def __init__(self):
#         print("demo")
#     def display(self):
#         print("Display")

# hp = Laptop()
# hp.display()

# ------------------

# class Laptop():
#     def __init__(self):        
#         self.ram = ""
#         self.processor = ""
#     def display(self):
#         print("Display: ")
#         print("ram :", self.ram)
#         print("processor : ",self.processor)
# hp = Laptop()
# hp.ram = "8GB"
# hp.processor = "i5"

# hp.display()


# -----------------
# class Laptop():
#     def __init__(self):        
#         self.ram = ""
#         self.processor = ""
#     def display(self):
#         print("Display: ")
#         print("ram :", self.ram)
#         print("processor : ",self.processor)
# hp = Laptop()
# dell = Laptop()
# hp.ram = "8GB"
# hp.processor = "i5"

# dell.ram = "12GB"
# dell.processor = "i7"

# hp.display()
# dell.display()

# ---------------
# class student():
#     def __init__(self):
#         self.name = "Ramu"
#         self.regno = "regno123"
#     def display(self):
#         print("Name :",self.name)
#         print("Reg no :",self.regno)

# s1 = student()
# s2 = student()
# s1.name = "Guru"
# s1.regno = "1"
# s2.name = "Karthi"
# s2.regno = "2"
# s1.display()
# s2.display()

# ----------------------

# class fruit():
#     def __init__(self):
#         self.color="black"

# apple=fruit()
# apple.color="red"
# print(apple.color)

# ------------------
# class fruit():
#     def __init__(self,color):
#         self.color=color

# apple=fruit("red")
# print(apple.color)

# --------------------
# class teacher():
#     def __init__(self,name,regno):
#         self.name = name
#         self.regno = regno
#     def display(self):
#         print("Name : ", self.name)
#         print("Regno : ",self.regno)

# t1=teacher("Sam","223")
# t2=teacher("Thomas","224")
# t1.display()
# t2.display()

# ---------------------
class calculator():
    def __init__(self,v1,v2):
        self.a = v1
        self.b = v2
    def add(self):
        print("add : ",self.a + self.b)
    def sub(self):
        print("sub : ", self.a - self.b)
    def mul(self):
        print("mul : ", self.a * self.b)
    def div(self):
        print("div : ",self.a /self.b)

c1 = calculator(int(2),int(3))
c1.add()
c1.sub()
c1.mul()
c1.div()
