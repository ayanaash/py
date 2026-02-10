#1
class Animal:
    def speak(self):
        print("I make a sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")    #заменил

d = Dog()
d.speak()   #'woof'

#2
class Animal:
    def __init__(self):
        print("Animal created")

class Dog(Animal):
    def __init__(self):
        print("Dog created")

d = Dog()   #Dog created

#3
class Animal:
    def speak(self):
        print("I make a sound")

class Dog(Animal):
    def speak(self):
        super().speak() 
        print("Woof!")

d = Dog()
d.speak()    #I make a sound \ Woof!


#4
class Animal:
    def __init__(self):
        print("Animal created")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog created")

d = Dog()     #Animal created \ Dog created



#5
class Animal:
    def greet(self, name):
        print("Hello", name)

class Dog(Animal):
    def greet(self, name):
        print("Woof! Hello", name)

d = Dog()
d.greet("Ayana")    #Woof! Hello Ayana