from MedicineCatalog import Medicine, Catalog

class Cart:
    def __init__(self):
        self.items = {}
    # default value set to 1
        
    def __str__(self):
        s = "Cart: " + self.displayCart()
        return s
        
    def __repr__(self):
        s = "Id<"+ str(id(self)) + "> " + self._items
        return s
    
    def addToCart(self, medicine, quantity=1):
        if medicine in self.items:
            self.items[medicine] += quantity
        else:
            self.items[medicine] = quantity


    def updateCart(self, medicine, quantity):
        if medicine in self.items:
            self.items[medicine] = quantity
        else:
            raise AttributeError("No such item found in Cart")

    def displayCart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Shopping Cart:","\n")
            for medicine, quantity in self.items.items():
                medicine.displayInfo()
                print(f"Quantity: {quantity}")
                print(f"Total Price: ${medicine.getPrice() * quantity}")