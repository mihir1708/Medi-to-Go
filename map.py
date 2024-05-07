def hospital():
    import tkinter as tk
    from tkinter import messagebox
    from tkintermapview import TkinterMapView
    import googlemaps
    from datetime import datetime

    class HospitalMapApp:
        def __init__(self, master):
            self.master = master
            self.master.title("Hospital Finder and Map")

            self.gmaps = googlemaps.Client(key='AIzaSyAdNNjKyPkvYb_ZbZ2cUrje8LDJsq3IHiI')

            self.user_lat = ''
            self.user_lng = ''
            self.hospitals = {}

            self.create_widgets()

        def create_widgets(self):
            # Hospital Finder widgets
            self.get_user_location()

            self.get_hospitals_button = tk.Button(self.master, text="Get Hospitals", command=self.get_hospitals)
            self.get_hospitals_button.pack(pady=10)

            self.hospitals_text = tk.Text(self.master, height=10, width=40)
            self.hospitals_text.pack(pady=10)

            self.select_hospital_label = tk.Label(self.master, text="Enter the number of the selected hospital:")
            self.select_hospital_label.pack(pady=5)

            self.hospital_choice_entry = tk.Entry(self.master)
            self.hospital_choice_entry.pack(pady=5)

            self.get_duration_distance_button = tk.Button(self.master, text="Get Duration and Distance", command=self.get_time_distance)
            self.get_duration_distance_button.pack(pady=10)

            self.result_label = tk.Label(self.master, text="")
            self.result_label.pack(pady=5)

            # Map widgets
            self.map_widget = TkinterMapView(self.master, width=800, height=600, corner_radius=0)
            self.map_widget.pack(pady=10)
            self.map_widget.set_address("Winnipeg, Manitoba, Canada")

        def get_user_location(self):
            try:
                location = self.gmaps.geolocate()
                self.user_lat = location["location"]["lat"]
                self.user_lng = location["location"]["lng"]
            except:
                messagebox.showerror("Error", "Unable to obtain user location")

        def get_hospitals(self):
            
            hospitals_temp = self.gmaps.places_nearby(location=(self.user_lat, self.user_lng), radius=100000, keyword="hospital", language="English")
            self.hospitals = {}
            if len(hospitals_temp['results']) > 0:
                for i, hospital_info in enumerate(hospitals_temp['results']):
                    hospital_name = hospital_info['name']
                    self.hospitals[i + 1] = {
                        'name': hospital_name,
                        'lat': hospital_info['geometry']['location']['lat'],
                        'lng': hospital_info['geometry']['location']['lng'],
                        'distance': self.gmaps.directions((self.user_lat, self.user_lng),
                                                        (hospital_info['geometry']['location']['lat'],
                                                        hospital_info['geometry']['location']['lng']),
                                                        departure_time=datetime.now(), mode="driving")[0]["legs"][0]["distance"]['text']
                    }
                    self.hospitals_text.insert(tk.END, f"{i + 1}. {hospital_name}\nDistance: {self.hospitals[i + 1]['distance']}\n\n")
                # Update map markers
                self.update_map_markers()
            else:
                messagebox.showinfo("No Hospitals", "No hospitals found in the vicinity.")
            

        def get_time_distance(self):
            try:
                choice = int(self.hospital_choice_entry.get())
                if choice in self.hospitals:
                    selected_hospital = self.hospitals[choice]
                    distance = self.gmaps.directions((self.user_lat, self.user_lng),
                                                    (selected_hospital['lat'], selected_hospital['lng']),
                                                    departure_time=datetime.now(), mode="driving")[0]["legs"][0]["distance"]['text']
                    duration = self.gmaps.directions((self.user_lat, self.user_lng),
                                                    (selected_hospital['lat'], selected_hospital['lng']),
                                                    departure_time=datetime.now(), mode="driving")[0]["legs"][0]["duration"]['text']
                    self.result_label.config(text=f"Selected Hospital: {selected_hospital['name']}\nDistance: {distance}\nDuration: {duration}")
                else:
                    messagebox.showerror("Error", "Please Enter a Valid Hospital Number!")
            except ValueError:
                messagebox.showerror("Error", "Please Enter a Numerical Value for Hospital Number")

        def update_map_markers(self):
            self.map_widget.clear_markers()
            for i, data in self.hospitals.items():
                lat, lng = data['lat'], data['lng']
                marker = self.map_widget.set_marker(lat, lng, text=f"{i}. {data['name']}")
                marker.set_text(f"{i}. {data['name']}")

    root = tk.Tk()
    app = HospitalMapApp(root)
    root.mainloop()
