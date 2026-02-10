#1
class Animal:
    kind = "Mammal"

class Dog(Animal):
    pass

d = Dog()
print(d.kind) #'mammal

#2
class Animal:
    def speak(self):
        print("I make a sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()   #'i make a sound'

#3
class Animal:
    def speak(self):
        print("I make a sound")

class Dog(Animal):
    def bark(self):
        print("Woof!")

d = Dog()
d.speak()
d.bark()     #'i make a sound \ woof!'

#4
class Animal:
    def speak(self):
        print("I make a sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

d = Dog()
d.speak()    #'woof!'

#5
class Animal:
    def __init__(self, kind):
        self.kind = kind

class Dog(Animal):
    pass

d = Dog("Mammal")
print(d.kind)   #'mammal'