class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f"{self.name} can makes a sound."
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


c = Animal("Generic Animal")
d = Dog("Buddy")
e = Cat("Whiskers")
print(d.speak())#out put: Buddy says Woof! 
print(e.speak())#out put :  Whiskers says Meow!
print(d.name)#out put: Buddy
print(e.name)#out put: Whiskerss
print(d.speak())#out put: Buddy says Woof!
print(e.sound())#out put: Whiskers can makes a sound.

#what is inheritancce here Class Animal is the parent class and Class Dog and Class Cat are the child classes. The child classes inherit the properties and methods of the parent class. In this case, the speak method is inherited by both Dog and Cat classes from the Animal class. However, both Dog and Cat classes override the speak method to provide their own implementation.

# inheritance means we can use the speak method of the parent class in the child class and we can also override the method in the child class