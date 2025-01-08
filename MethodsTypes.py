# class laptop():
#     chargertype ="C-TYPE"
    
#     def __init__(self):
#         self.brand=""
#         self.price=34
#     def setPrice(self,price):
#         self.price=price
#     def getPrice(self):
#         print(self.price)

# hp=laptop()
# hp.setPrice(20000)
# hp.getPrice()


# --------------------

# class laptop():
#     chargertype ="C-TYPE"
    
#     def __init__(self):
#         self.brand=""
#         self.price=34
#     def setPrice(self,price):
#         self.price=price
#     def getPrice(self):
#         print(self.price)
        
#     def changeChargerType(cls):
#         cls.chargertype="B-TYPE"
#         print("Charger type changed to B")
        

# hp=laptop()
# hp.setPrice(20000)
# hp.getPrice()

# laptop.changeChargerType(laptop)


# --------------------
# class laptop():
#     chargertype ="C-TYPE"
    
#     def __init__(self):
#         self.brand=""
#         self.price=34
#     def setPrice(self,price):
#         self.price=price
#     def getPrice(self):
#         print(self.price)
        
#     @classmethod #decoraders
#     def changeChargerType(cls):
#         cls.chargertype="B-TYPE"
#         print("Charger type changed to B")
        

# hp=laptop()
# hp.setPrice(20000)
# hp.getPrice()

# laptop.changeChargerType()


# ------------------------------

class laptop():
    chargertype ="C-TYPE"
    
    def __init__(self):
        self.brand=""
        self.price=34
    def setPrice(self,price):
        self.price=price
    def getPrice(self):
        print(self.price)
        
    @classmethod #decoraders
    def changeChargerType(cls):
        cls.chargertype="B-TYPE"
        print("Charger type changed to B")
        
    @staticmethod
    def info():
        print("This is laptop class")
        

hp=laptop()
hp.setPrice(20000)
hp.getPrice()

laptop.changeChargerType()

hp.info()