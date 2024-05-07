import tkinter as tk
from Consultations import consultations  # Import the consultations function
from Catalog_page import catalog
from map import hospital

def show_main_page():
    def book_consultation():
        # root.destroy()
        consultations()

    def buy_medicines():
        # root.destroy()
        catalog()

    def go_to_hospital():
        # root.destroy()
        hospital()

    # Create the main window
    root = tk.Tk()
    root.title("Medi-To-Go")
    root.geometry("600x400")

    # Create a top bar
    top_bar = tk.Frame(root, bg="#3498db", height=50)
    top_bar.pack(side="top", fill="x")

    # Add text to the top left of the bar
    title_label = tk.Label(top_bar, text="Medi-To-Go", font=("Georgia", 18), padx=10, pady=10, bg="#3498db")
    title_label.pack(side="left")

    # Create a frame to hold the buttons and center it vertically
    button_frame = tk.Frame(root, pady=20)
    button_frame.pack(expand=True, fill="both", side="top", anchor="n")

    # Button 1: Book a Consultation
    consultation_button = tk.Button(button_frame, text="Book a Consultation", command=book_consultation, width=20, height=3)
    consultation_button.pack(side="left", padx=10)

    # Button 2: Buy Medicines
    medicines_button = tk.Button(button_frame, text="Buy Medicines", command=buy_medicines, width=20, height=3)
    medicines_button.pack(side="left", padx=10)

    # Button 3: Go to a Hospital (centered below the first two buttons)
    hospital_button = tk.Button(button_frame, text="Go to a Hospital", command=go_to_hospital, width=20, height=3)
    hospital_button.pack(side="left", padx=10)

    # Set rounded corners
    for button in [consultation_button, medicines_button, hospital_button]:
        button.config(borderwidth=5, relief="ridge", bd=5, padx=10, pady=10)

    # Start the Tkinter event loop
    root.mainloop()
