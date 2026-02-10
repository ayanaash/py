#1
def my_function(fname):
  print(fname + " hii")
my_function("ayana")
my_function('anaya')

#2
def my_function(name, /):
  print("Hello", name)

my_function("Emil")  # элементы до '/' только pos args

#3
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")  #keyword arg

#4
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")  #positional arg

#5
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)