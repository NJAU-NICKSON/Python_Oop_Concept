# Base class
class Animal:
    # The move method is defined but not implemented here.
    def move(self):
        pass

# Subclass representing a Dog
class Dog(Animal):
    def move(self):
        print("Dog is running")

# Subclass representing a Fish
class Fish(Animal):
    def move(self):
        print("Fish is swimming")


# Subclass representing a Bird
class Bird(Animal):
    def move(self):
        print("Bird is flying")

# Subclass representing a Snake
class Snake(Animal):
    def move(self):
        print("Snake is slithering")

# Subclass representing a Horse
class Horse(Animal):
    def move(self):
        print("Horse is galloping")


# Subclass representing a Kangaroo
class Kangaroo(Animal):
    def move(self):
        print("Kangaroo is hopping")


# Demonstration of polymorphism

animals = [Dog(), Fish(), Bird(), Snake(), Horse(), Kangaroo()]

# Even though they are all stored in one list,each object calls its own move() method.

for a in animals:
    a.move()
