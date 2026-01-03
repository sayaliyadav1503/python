#polymorphism
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.sound()


###
class Bike:
    def speed(self):
        print("Bike speed is 80 km/h")

class Car:
    def speed(self):
        print("Car speed is 120 km/h")

def show_speed(vehicle):
    vehicle.speed()

show_speed(Bike())
show_speed(Car())
