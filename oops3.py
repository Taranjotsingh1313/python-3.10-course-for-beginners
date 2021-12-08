# ATTRIBUTES IN CLASSES
'''
    1) INSTANCE ATTRIBUTE
    2) CLASS ATTRIBUTES
'''

# INSTANCE ATTRIBUTE

class Item:
    price  = 500


phone = Item()
phone.name = 'Iphone 13'
print(phone.price)

print("---------")
table = Item()
table.name = "Computer Table"
table.price = 200
print(table.price)