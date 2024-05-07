from MedicineCatalog import Medicine, Catalog
from Cart import Cart

def UserAddsToCart(medicine,quantity,catalog,cart):
    if (medicine in catalog.getMedicinesInventory() and quantity < catalog.getMedicinesInventory()[medicine]):
        cart.addToCart(medicine,quantity)
        catalog.updateCatalog(medicine,(catalog.getMedicinesInventory()[medicine] - quantity))
    else:
        raise AttributeError("Not Valid")
        
# Init catalog
catalog = Catalog()

# Medicine Log
Paracetamol = Medicine("Paracetamol", "Pharma", 3.00, "Pain reliever")
Amoxicillin = Medicine("Amoxicillin 500mg", "Amoxi", 4.00, "Anti Body")
Vyzulta = Medicine("Vyzulta","Bausch & Lomb Inc",4.00,"Eyedrop")
Cresemba = Medicine("Cresemba","Avir Pharma",5.00,"Anti Fungal")
Belsomra = Medicine("Belsomra","Merck Canada Inc",2.60,"Insomnia Relief")
Folotyn = Medicine("Folotyn","Servierer Canada Inc",3.55,"Cancer Treatment")

catalog.addMedicineInventory(Paracetamol,value=27)
catalog.addMedicineInventory(Amoxicillin,value=20)
catalog.addMedicineInventory(Vyzulta,value=12)
catalog.addMedicineInventory(Cresemba,value=15)
catalog.addMedicineInventory(Belsomra,value=25)
catalog.addMedicineInventory(Folotyn,value=15)

# Display
catalog.displayCatalog()

# Init Cart
cart = Cart()

cart.displayCart()
