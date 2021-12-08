# inheritance in oops

class Item:
    price = 500
    quality_good = True

    def printHello(self):
        print("Hello")

class Phone(Item):
    price = 600

Iphone = Phone()
Iphone.printHello()