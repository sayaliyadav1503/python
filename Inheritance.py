class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):   # Inheritance
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)   # Call parent constructor
        self.roll_no = roll_no

    def show_student(self):
        print("Roll No:", self.roll_no)


# Object creation
s1 = Student("Sayali", 21, 101)

s1.show_details()   # Parent method
s1.show_student()   # Child method
