# class company():
#     def __init__(self):
#         self.companyName ="Google"

# c1 = company()
# print(c1.companyName)

# ------------------------

# class company():
#     def __init__(self):
#         self.__companyName ="Google"
#     def companyName(self):
#         print(self.__companyName)

# c1 = company()
# c1.companyName()
# # print(c1.companyName)


# ----------------------------

class company():
    def __init__(self):
        self._companyName ="Google"    

class b(company):
    pass

b1 = b()
print(b1._companyName)