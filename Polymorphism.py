# def a(a,b,c=0):
#     print("test: ",a+b+c)
    
# a(10,30,30)

# Two word polymorphism means having many forms.
# In programming, polymorphism means the same function name (but different signatures)being 
# used for different types.
# The key difference is the data types and number of arguments used in function.

# class Animal():
#     def sound(self):
#         print("Animal makes sound")

# a1 = Animal()
# a1.sound()


#------------------------------

# class Animal():
#     def sound(self):
#         print("Animal makes sound")
        
# class Dog(Animal):
#     pass
    

# d1 = Dog()
# d1.sound()

# ---------------------------------
# method overridding
# class Animal():
#     def sound(self):
#         print("Animal makes sound")
        
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
    

# d1 = Dog()
# d1.sound()

# -----------------------
# class Animal():
#     def sound(self):
#         print("Animal makes sound")
        
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Bird(Animal):
#     def sound(self):
#         print("Birds Sing")
    

# b1 = Bird()
# b1.sound()

# --------------------------
# class Shape():
#     def area(self):
#         return 0    

    
# s1=Shape()
# res =s1.area()
# print(res)


# ---------------------------
# class Shape():
#     def area(self):
#         return 0
    
# class Rectangle(Shape):
#     def area(self):
#         l=10
#         b=20
#         return l*b
    
# r1=Rectangle()
# res =r1.area()
# print(res)

# ----------------------
# class Person():
#     def __init__(self,name):
#         self.name=name

# class Student(Person):
#     def __init__(self, name, grade):
#         super().__init__(name)
#         self.grade=grade
#     def display(self):
#         print(self.name,self.grade)
        
# s1 = Student("Jaman","A")
# s1.display()

# ----------------------------
# class Vehicle():
#     def start(self):
#         print("Vehicle started")

# class Car(Vehicle):
#     def start(self):
#         print("Car started")

# c1=Car()
# c1.start()

# ----------------------
# class Employee():
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
        
# class Manager(Employee):
#     def __init__(self,department):
#         super().__init__(self.name,self.salary)        
#         self.department=department
#     def display(self):
#         print(self.name,self.salary,self.department)

# m1=Manager("Jaman","Salary","CSE")
# m1.display()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
class Manager(Employee):
    def __init__(self, name, salary, department):
        # Pass 'name' and 'salary' to the parent class
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")

# Create a Manager instance with valid arguments
m1 = Manager("Jaman", 50000, "CSE")
m1.display()
