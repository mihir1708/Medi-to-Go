import tkinter as tk
from tkinter import simpledialog, messagebox
from tkcalendar import DateEntry  # Import the DateEntry widget
from datetime import datetime
from time import strftime
from Doctors import Availability

def consultations():
    class TimePicker(tk.Toplevel):
        """Custom dialog to pick the time."""

        def __init__(self, master, *args, **kwargs):
            super().__init__(master, *args, **kwargs)
            self.title("Pick Time")

            tk.Label(self, text="Select Time:", font=("Helvetica", 14)).pack(pady=10)

            self.time_var = tk.StringVar()
            self.time_var.set(strftime('%H:%M'))

            time_entry = tk.Entry(self, textvariable=self.time_var)
            time_entry.pack(pady=5)

            ok_button = tk.Button(self, text="OK", command=self.ok)
            ok_button.pack(pady=10)

        def ok(self):
            """Handle the OK button click."""
            selected_time = self.time_var.get()
            try:
                datetime.strptime(selected_time, '%H:%M')
                self.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid time format. Please use HH:MM.")


    class DoctorButton(tk.Button):
        """Custom Button class to open a new window for doctor consultation scheduling."""

        def __init__(self, master, doctor, *args, **kwargs):
            super().__init__(master, text=f"{doctor.name}\n{doctor.exp} in {doctor.spec}", command=lambda: self.schedule_consultation(doctor), *args, **kwargs)
            self.doctor = doctor

        def validate_date(self, date):
            """Validate that the selected date is not in the past."""
            try:
                selected_date = datetime.strptime(date, "%m/%d/%y")
                current_date = datetime.now()
                return selected_date >= current_date
            except ValueError:
                return False

        def show_time_picker(self):
            """Show the custom time picker dialog."""
            time_picker = TimePicker(self.master)
            self.master.wait_window(time_picker)
            return time_picker.time_var.get()

        def schedule_consultation(self, doctor):
            """Open a new window for scheduling a consultation with the selected doctor."""
            consultation_window = tk.Toplevel(root)
            consultation_window.title("Schedule Consultation")

            tk.Label(consultation_window, text=f"Schedule Consultation with {doctor.name}", font=("Helvetica", 14)).pack(pady=10)

            date_entry = DateEntry(consultation_window, width=20, background='darkblue', foreground='white', borderwidth=2)
            date_entry.pack(pady=5)

            time_var = tk.StringVar()

            tk.Label(consultation_window, text="Time:").pack(pady=5)
            time_entry = tk.Entry(consultation_window, textvariable=time_var, state="readonly")
            time_entry.bind("<Button-1>", lambda event: time_var.set(self.show_time_picker()))
            time_entry.pack(pady=5)

            schedule_button = tk.Button(consultation_window, text="Schedule", command=lambda: self.schedule_action(doctor, date_entry.get(), time_var.get()))
            schedule_button.pack(pady=10)

        def schedule_action(self, doctor, date, time):
            """Handle the scheduling action for the consultation."""
            if not self.validate_date(date):
                messagebox.showerror("Error", "Please select a future date.")
                return

            if not time:
                messagebox.showerror("Error", "Please select a time.")
                return

            success_message = f"Scheduled consultation with {doctor.name} on {date} at {time}"
            messagebox.showinfo("Success", success_message)

    root = tk.Tk()
    root.title("Doctor Information")
    root.geometry("700x300")

    frame_buttons = tk.Frame(root)
    frame_buttons.pack(pady=20)

    doctors_list = [
        Availability(name="Dr. Jai Ohri", experience="15 Years",
                    speciality="Computational Cognitive Psychology",
                    availability=["Mon 10:00 AM - 12:00 PM", "Wed 2:00 PM - 4:00 PM"]),
        Availability(name="Dr. Abhishekh Jayaprakash", experience="14 Years",
                    speciality="Radiology",
                    availability=["Tue 9:00 AM - 11:00 AM", "Thu 3:00 PM - 5:00 PM"]),
        Availability(name="Dr. Mihir Mukhi", experience="10 Years",
                    speciality="Physician",
                    availability=["Tue 11:00 AM - 2:00 PM", "Fri 7:00 PM - 9:00 PM"]),
        Availability(name="Dr. Devansh Artwanni", experience="12 Years",
                    speciality="Sensory Processing",
                    availability=["Sat 8:00 AM - 12:00 PM", "Sun 4:00 PM - 9:00 PM"])
        # Add more doctors with availability as needed
    ]

    buttons = []

    for i, doctor in enumerate(doctors_list):
        button = DoctorButton(frame_buttons, doctor, width=40, height=4)
        buttons.append(button)
        button.grid(row=i // 2, column=i % 2, padx=(10, 20), pady=10)

    root.mainloop()
