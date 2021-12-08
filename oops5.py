# CONTSTRUCTOR IN CLASSES

# CONTSTRUCTOR IS METHOD IN CLASSES WHICH RUNS IMMEDIATELY WHENEVER INSTANCE OF CLASS IS CREATED

class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    price  = 500

phone = Item("Iphone 13",500)
table = Item("Pc Table",200)
print(phone.name)
print(phone.price)
print(table.name)
print(table.price)