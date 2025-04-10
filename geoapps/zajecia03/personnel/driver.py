# V1 - slajd 8: python -m personnel.driver
from .employee import Employee

class Driver(Employee):
    def __init__(self, first_name, last_name, employee_id, salary, license_number, qualifications):
        # alternatywa: super().__init__(self, ...)
        Employee.__init__(self, first_name, last_name, employee_id, salary)
        self.license_number = license_number
        self.qualifications = qualifications

    def display_info(self):
        return f"Driver ID: {self.employee_id}, Name: {self.first_name} {self.last_name}, Salary: {self.salary}, License Number: {self.license_number}, Qualifications: {', '.join(self.qualifications)}"

# Uruchomienie tego kodu: python -m geoapps.zajecia03.personnel.driver
if __name__ == "__main__":
    driver1 = Driver("Jane", "Smith", 1, 12000.00, "LIC1001", ["BLS"])
    print(driver1.display_info())
