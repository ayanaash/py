#1
x = lambda a : a + 10
print(x(5))

#2
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#3
x = lambda a : a * a
print(x(8))

#4
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#5
def f(n):
    return lambda a : a - n
d = f(3)  # n = 3
print(d(8))  # a = 8