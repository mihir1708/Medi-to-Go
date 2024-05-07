class Doctor:
    """Class to represent a healthcare professional."""

    def __init__(self, name="", experience="", speciality=""):
        self.name = name
        self.exp = experience
        self.spec = speciality
        self.doctor_info = {}

    def set_info(self):
        """Set the information for the doctor."""
        self.doctor_info = {"Name": self.name, "Experience": self.exp, "Specialization": self.spec}

    def print_info(self):
        """Print the information for the doctor."""
        print(self.doctor_info)


class Availability(Doctor):
    """Class to manage the availability of a healthcare professional."""

    def __init__(self, name="", experience="", speciality="", availability=None):
        super().__init__(name, experience, speciality)
        self.avail = availability or []

    def add_availability(self, time_slot):
        """Add a time slot to the availability."""
        self.avail.append(time_slot)

    def get_availability(self):
        """Retrieve the current availability."""
        return self.avail


if __name__ == "__main__":
    doctor1 = Availability(name="Dr. Jai Ohri", experience="15 Years",
                            # speciality="memory, sensory processing, computational cognitive psychology",
                            speciality="Computational Cognitive Psychology",
                            availability=["Mon 10:00 AM - 12:00 PM", "Wed 2:00 PM - 4:00 PM"])
    doctor1.set_info()
    doctor1.print_info()
    print("Availability:", doctor1.get_availability())

    doctor2 = Availability(name="Dr. Abhishekh Jayaprakash", experience="14 Years",
                            # speciality="Radiology, Bone densitometry, Cardiac-interventional radiography, Computed tomography (CT), Magnetic resonance imaging (MRI)",
                            speciality="Radiology",
                            availability=["Tue 9:00 AM - 11:00 AM", "Thu 3:00 PM - 5:00 PM"])
    doctor2.set_info()
    doctor2.print_info()
    print("Availability:", doctor2.get_availability())

    doctor3 = Availability(name="Dr. Mihir Mukhi", experience="10 Years",
                            speciality="Physician",
                            availability=["Tue 11:00 AM - 14:00 AM", "Fri 7:00 PM - 9:00 PM"])
    doctor3.set_info()
    doctor3.print_info()
    print("Availability:", doctor3.get_availability())

    doctor4 = Availability(name="Dr. Devansh Artwanni", experience="12 Years",
                            speciality="Sensory Processing",
                            availability=["Sat 08:00 AM - 12:00 PM", "Sun 4:00 PM - 9:00 PM"])
    doctor4.set_info()
    doctor4.print_info()
    print("Availability:", doctor4.get_availability())

    # Add more doctors with availability as needed