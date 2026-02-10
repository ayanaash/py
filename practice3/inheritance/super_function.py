#1
class Animal:
    def __init__(self):
        print("Animal created")

class Dog(Animal):
    def __init__(self):
        super().__init__()  #call __init__ of parent
        print("Dog created")

d = Dog()     #Animal created \ Dog created


#2
class Animal:
    def __init__(self, kind):
        print("Animal:", kind)

class Dog(Animal):
    def __init__(self, kind, name):
        super().__init__(kind)  
        print("Dog:", name)

d = Dog("Mammal", "Buddy")     #Animal: Mammal \ Dog: Buddy


#3
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()  
        print("Woof!")

d = Dog()
d.speak()     #Animal sound \ Woof!


#4
class Animal:
    def __init__(self, kind):
        self.kind = kind

class Dog(Animal):
    def __init__(self, kind, name):
        super().__init__(kind)
        self.name = name

d = Dog("Mammal", "Buddy")
print(d.kind, d.name)      #Mammal Buddy


#5
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Dog sound")   #firstly child
        super().speak()      #after, parent

d = Dog()
d.speak()    #Dog sound \ Animal sound