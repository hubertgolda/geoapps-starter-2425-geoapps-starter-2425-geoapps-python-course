from geoapps.zajecia03.fleet.ambulance import Ambulance
from geoapps.zajecia03.operations import *
from geoapps.zajecia03.personnel import *


def run_application():
    # Zdefiniowanie naszych zasobów
    ambulance1 = Ambulance(1, "Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance(2, "Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])

    employee1 = Employee("John", "Doe", 123, 12000.0)
    employee2 = Employee("Jane", "Smith", 124, 8000.0)

    driver1 = Driver("Mike", "Johnson", 125, 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "Brown", 126, 11500.0, "DL12346", ["ALS", "PHTLS"])

    # Sprawdzenie czy to czasem nie są te same karetki
    if ambulance1 == ambulance2:
        raise ValueError("To są te same karetki!")
    # Sprawdzenie ile mamy karetek
    print(Ambulance.get_instances_count())

    # Stworzenie kolejki
    queue = IncidentQueue()

    # Zaraportowanie 2 zgłoszeń
    incident1 = Incident(1, "Power outage in sector 4")
    incident2 = Incident(2, "Fire alarm in building 21")
    queue += incident1
    queue += incident2

    # Wypisz wszystkie zgłoszenia
    print("Aktualne zgłoszenia:")
    print(queue)

    # Daj kierowcy podwyżkę za super zasługi
    print(f"Przed podwyżką: {driver1.display_info()}")
    driver1.update_salary(5000.12)
    print(f"Po podwyżce: {driver1.display_info()}")


if __name__ == "__main__":
    run_application()