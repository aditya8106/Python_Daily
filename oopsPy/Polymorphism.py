#Polymorphism in Python is the ability of an object to take on many forms. It allows us to define methods in the child class with the same name as defined in their parent class. This means that a method can have different implementations based on the object that is calling it.

class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")
    def sound(self):
        return f"{self.name} can makes a sound."

class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
def animal_sound(animal):
    print(animal.speak())


dog = Dog()
cat = Cat()
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!