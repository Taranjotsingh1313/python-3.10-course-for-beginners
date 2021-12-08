# METHODS IN CLASS
# FUNCTIONS IN CLASSES ARE KNOWN AS METHODS
def function():
    print("functuion run hua hai")



class Item:
    price  = 500

    def clasFunc(self):
        print(f"Name of object is {self.name}")

table = Item()
table.name = "Computer Table"
phone = Item()
phone.name = 'Iphone 13'
table.clasFunc()
phone.clasFunc()