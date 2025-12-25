class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        self.address = self.Address()   # creating object of inner class

    def show_employee(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        self.address.show_address()

    # Inner Class
    class Address:
        def __init__(self):
            self.city = "pune"
            self.state = "Maharashtra"

        def show_address(self):
            print("City:", self.city)
            print("State:", self.state)


# Creating object of outer class
emp = Employee("Sayali", 101)
emp.show_employee()
