class Ambulance:
    # __slots__ = ['id', 'vehicle_type', 'status', 'location', 'medical_equipment']
    __instances_count = 0

    def __init__(self, id, vehicle_type, status, location, medical_equipment):
        self.id = id
        self.vehicle_type = vehicle_type
        self.status = status  # e.g., "available", "on_mission", "servicing"
        self.location = location # as (northing, easting)
        self.medical_equipment = medical_equipment  # List of medical equipment names
        Ambulance.__instances_count += 1

    def update_location(self, new_location):
        self.location = new_location

    def __eq__(self, other):
        if not isinstance(other, Ambulance):
            return NotImplemented
        return self.id == other.id and self.vehicle_type == other.vehicle_type
    
    def __str__(self):
        return (f"Ambulance ID: {self.id}, Type: {self.vehicle_type}, "
                f"Status: {self.status}, Location: {self.location}, "
                f"Equipment: {', '.join(self.medical_equipment)}")
    
    @staticmethod
    def validate_id(ambulance_id):
        return isinstance(ambulance_id, int) and ambulance_id > 0

    @classmethod
    def get_instances_count(cls):
        return f"Number of working ambulances: {cls.__instances_count}"

# Uruchomienie tej czesci jak zwyklego skryptu
if __name__ == "__main__":
    ambulance1 = Ambulance(
        id=0,
        vehicle_type="AZ124",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment = ["defibrillator", "stretcher"]
    )
    ambulance2 = Ambulance(
        id=1,
        vehicle_type="AZ2000",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment = ["defibrillator", "stretcher"]
    )

    print(ambulance1 == ambulance2)
    print(ambulance1)

# sloty - odkomentować __slots__
    # ambulance1.whatever = "123"
    # print(ambulance1.whatever)

# metody statyczne i metody klasy
    print(Ambulance.validate_id(123))
    print(Ambulance.validate_id("123"))

    print(Ambulance.get_instances_count())