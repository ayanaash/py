#1
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")    # '*' можно писать несколько

#2
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

#3
def f(**kwargs):
    print(kwargs)
f(a=1, b=2)   #{'a': 1, 'b': 2}

#4
def f(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
f(x=10, y=20)   #x 10, y 20

#5
def f(**data):
    print(data.get('name'))
f(name = 'Ayana', age = 17)  #'Ayana'