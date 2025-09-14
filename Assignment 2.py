class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car is starting")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting")


v = Vehicle()
v.start()

c = Car()
c.start()

b = Bike()
b.start()





class Circle:
    def _init_(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle:
    def _init_(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total


shapes = [Circle(2), Rectangle(4, 5), Circle(1)]
print("Total area:", total_area(shapes))





class Shape:
    def init(self):
        print("Shape created")

class Rectangle(Shape):
    def init(self, width, height):
        super().init()  # Calls Shape's constructor
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


r = Rectangle(3, 4)
print("Area:", r.calculate_area())





class Dog:
    def make_sound(self):
        print("Woof!")

class Cat:
    def make_sound(self):
        print("Meow!")

def process_sound(animal):
    animal.make_sound()


d = Dog()
c = Cat()

process_sound(d)
process_sound(c)





class FileHandler:
    def read(self):
        pass

    def write(self, data):
        pass

class TextFileHandler(FileHandler):
    def read(self):
        print("Reading text")

    def write(self, data):
        print("Writing text:", data)

class BinaryFileHandler(FileHandler):
    def read(self):
        print("Reading binary")

    def write(self, data):
        print("Writing binary:", data)


t = TextFileHandler()
t.read()
t.write("Hello")

b = BinaryFileHandler()
b.read()
b.write("101010")









