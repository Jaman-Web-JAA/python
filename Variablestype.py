# class phone():
#     def __init__(self,brand,price,chargertype):
#         self.brand = brand
#         self.price = price
#         self.chargertype = chargertype
#     def display(self):
#             print("Brand:", self.brand)
#             print("Price:",self.price)
#             print("chargertype:",self.chargertype)

# samsung = phone("Samsung","10000","B-Type")
# samsung.display()


# ------------------------
class phone():
    chargertype = "C-Type"
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def display(self):
            print("Brand:", self.brand)
            print("Price:",self.price)
            print("chargertype:",self.chargertype)

phone.chargertype = "B-TYPE"

samsung = phone("Samsung","10000")
samsung.display()

redmi = phone("Redmi","12000")
samsung.display()