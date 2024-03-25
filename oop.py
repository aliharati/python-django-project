class Animal:

    def __init__(self, legs) -> None:
        self.legs = legs
    
    def eat():
        print("eating")

class Dog(Animal):
    # CLASS OBJECT ATTRIBUTE
    species = "mammal"
    def __init__(self,legs, breed, name="rex"):
        super().__init__(legs)
        self.breed = breed
        self.name = name
    def bark(self):
        print('Woof Woof')
    def announce_breed(self):
        print(self.breed)
    def say_hi():
        print('hi')


class Circle():
    pi = 3.14

    def __init__(self, radius) -> None:
        self.radius =radius

    def area(self):
        return self.radius**2*Circle.pi
    
    def set_radius(self,val):
        self.radius = val

class Book:
    def __init__(self, name, author, pages) -> None:
        self.name = name
        self.author = author
        self.pages = pages       
    
    def __str__(self) -> str:
        return f"Title: {self.name} Author: {self.author} Pages: {self.pages}"

    def __len__(self) -> int:
        return self.pages

dog = Dog(4,"lab")
dog.bark()
dog.announce_breed()
print(Dog.species)
print(Dog.say_hi())
print(dog.legs)
# circle = Circle(3)
# print(circle.area())

book = Book("1984", "Orwell", 400)
print(book)
print(len(book))