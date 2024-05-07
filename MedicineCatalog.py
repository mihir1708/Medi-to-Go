class Catalog():
    def __init__(self):
        self._medicines = {}

    def __str__(self):
        s = "Catalog: " + self.displayCatalog()
        return s
        
    def __repr__(self):
        s = "Id<"+ str(id(self)) + "> " + self._medicines
        return s

    def addMedicineInventory(self, medicine, value=1):
        self._medicines[medicine] = value

    def updateCatalog(self,medicine,value):
        if (medicine in  self._medicines):
            self._medicines[medicine] = value        

    def getMedicinesInventory(self):
        return self._medicines

    def displayCatalog(self):
        print("Medicine Catalog:","\n")
        for medicine in self._medicines:
            medicine.displayInfo()
            print("")
    
    

class Medicine(Catalog):

    def __init__(self, name, manufacturer, price, description):
        self._name = name
        self._manufacturer = manufacturer
        self._price = price
        self._description = description
        
    # getters and setters
    def getName(self):
        return self._name

    def setName(self, value):
        self._name = value

    def getManufacturer(self):
        return self._manufacturer

    def setManufacturer(self, value):
        self._manufacturer = value

    def getPrice(self):
        return self._price

    def setPrice(self, value):
        self._price = value

    def getDescription(self):
        return self._description

    def setDescription(self, value):
        self._description = value

    def displayInfo(self):
        print(f"Name: {self._name}")
        print(f"Manufacturer: {self._manufacturer}")
        print(f"Price: ${self._price}")
        print(f"Description: {self._description}")
# Test run
        '''
catalog = Catalog()

Paracetamol = Medicine("Paracetamol", "MAN", 3.00, "Pain reliever")
Ibuprofen = Medicine("Amoxicillin 500mg", "MAN", 4.00, "Anti Body")

catalog.addMedicineInventory(Paracetamol,5)
catalog.addMedicineInventory(Ibuprofen,3)

# Displaying the catalog
catalog.displayCatalog()
'''
