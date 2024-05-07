def catalog():
    import tkinter as tk
    from tkinter import simpledialog, messagebox
    from User import catalog, UserAddsToCart, cart

    class QuantityDialog(simpledialog.Dialog):
        def __init__(self, parent, medicine):
            self.medicine = medicine
            super().__init__(parent)

        def body(self, master):
            tk.Label(master, text=f"Quantity of {self.medicine.getName()}:",
                    font=("Helvetica", 14)).grid(row=0)
            self.entry = tk.Entry(master)
            self.entry.grid(row=0, column=1)
            return self.entry

        def apply(self):
            try:
                value = int(self.entry.get())
                self.result = value
            except ValueError:
                self.result = None

    class MedicineApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Medicine Catalog")

            # Initialize catalog
            self.catalog = catalog

            # Create a frame to contain each pair of medicine buttons
            medicine_frame = tk.Frame(root)
            medicine_frame.pack()

            # Create buttons for each medicine, arranging them two in one horizontal line
            for i, medicine in enumerate(self.catalog.getMedicinesInventory()):
                if i % 2 == 0:
                    # Create a new frame for each pair of buttons
                    frame = tk.Frame(medicine_frame)
                    frame.pack(side="top", pady=10)

                button_text = f"{medicine.getName()} - ${medicine.getPrice()} per unit"
                button = tk.Button(frame, text=button_text, command=lambda m=medicine: self.add_to_cart(m), font=("Helvetica", 12))
                button.pack(side="left", padx=10, anchor="center")

            # Create View Cart button with extra spacing
            view_cart_button = tk.Button(root, text="View Cart", command=self.view_cart, font=("Helvetica", 16))
            view_cart_button.pack(pady=20, anchor="center")

        def add_to_cart(self, medicine):
            try:
                # Prompt user for quantity using custom dialog
                dialog = QuantityDialog(self.root, medicine)
                quantity = dialog.result
                if quantity is not None:
                    UserAddsToCart(medicine, quantity, self.catalog, cart)
                    messagebox.showinfo("Success", f"{quantity} {medicine.getName()} added to cart.")
            except AttributeError:
                messagebox.showerror("Error", "Medicine not added to cart. Not enough stock.")

        def view_cart(self):
            if cart.items:
                cart_window = tk.Toplevel(self.root)
                cart_window.title("View Cart")

                total_price = 0

                for medicine, quantity in cart.items.items():
                    item_label = tk.Label(cart_window, text=f"{quantity} {medicine.getName()} - Total Price: ${round(medicine.getPrice() * quantity, 2)}", font=("Helvetica", 12))
                    item_label.pack()
                    total_price += round(medicine.getPrice() * quantity, 2)

                total_label = tk.Label(cart_window, text=f"Total Price: ${total_price}", font=("Helvetica", 14))
                total_label.pack()

                # Add Buy Now button
                buy_now_button = tk.Button(cart_window, text="Buy Now", command=lambda: self.buy_now(cart_window), font=("Helvetica", 14))
                buy_now_button.pack(pady=10)

                return cart_window
            else:
                empty_cart_window = tk.Toplevel(self.root)
                empty_cart_window.title("Empty Cart")

                empty_label = tk.Label(empty_cart_window, text="Your cart is empty.", font=("Helvetica", 16))
                empty_label.pack(padx=20, pady=20)

        def buy_now(self, cart_window):
            address_window = tk.Toplevel(self.root)
            address_window.title("Enter Your Address")
            address_window.geometry("400x200")  # Set size of the address window

            # Address Line 1
            address1_label = tk.Label(address_window, text="Address Line 1:", font=("Helvetica", 12))
            address1_label.grid(row=0, column=0, sticky="w")
            address1_entry = tk.Entry(address_window)
            address1_entry.grid(row=0, column=1, padx=5, pady=5)

            # Address Line 2
            address2_label = tk.Label(address_window, text="Address Line 2:", font=("Helvetica", 12))
            address2_label.grid(row=1, column=0, sticky="w")
            address2_entry = tk.Entry(address_window)
            address2_entry.grid(row=1, column=1, padx=5, pady=5)

            # City
            city_label = tk.Label(address_window, text="City:", font=("Helvetica", 12))
            city_label.grid(row=2, column=0, sticky="w")
            city_entry = tk.Entry(address_window)
            city_entry.grid(row=2, column=1, padx=5, pady=5)

            # Province
            province_label = tk.Label(address_window, text="Province:", font=("Helvetica", 12))
            province_label.grid(row=3, column=0, sticky="w")
            province_entry = tk.Entry(address_window)
            province_entry.grid(row=3, column=1, padx=5, pady=5)

            # Postal Code
            postal_label = tk.Label(address_window, text="Postal Code:", font=("Helvetica", 12))
            postal_label.grid(row=4, column=0, sticky="w")
            postal_entry = tk.Entry(address_window)
            postal_entry.grid(row=4, column=1, padx=5, pady=5)

            # Confirm Buy button
            confirm_button = tk.Button(address_window, text="Confirm Buy", command=lambda: self.confirm_buy(address1_entry.get(), address2_entry.get(), city_entry.get(), province_entry.get(), postal_entry.get(), address_window, cart_window), font=("Helvetica", 14))
            confirm_button.grid(row=5, column=1, padx=5, pady=10, sticky="e")

            # Total Price Label
            total_label = tk.Label(address_window, text=f"Total: ${self.calculate_total_price()}", font=("Helvetica", 12))
            total_label.grid(row=5, column=2, padx=20, pady=10, sticky="e")

        def calculate_total_price(self):
            total_price = sum(round(medicine.getPrice() * quantity, 2) for medicine, quantity in cart.items.items())
            return total_price
        
        def confirm_buy(self, address1, address2, city, province, postal, address_window, cart_window):
            if address1 and city and province and postal:
                messagebox.showinfo("Thank You", "Thank you for purchasing!")
                cart.items = {}  # Reset cart to empty
                address_window.destroy()
                cart_window.destroy()  # Close the cart window
            else:
                messagebox.showerror("Error", "Please fill in all required fields.")

    root = tk.Tk()
    app = MedicineApp(root)

    # Set the initial size of the window
    root.geometry("600x400")

    root.mainloop()
