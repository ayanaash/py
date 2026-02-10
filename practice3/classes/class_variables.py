#1
class A:
    x = 10

print(A.x)


#2
class A:
    x = 10  # class variable

a1 = A()
a2 = A()
print(a1.x, a2.x)


#3
class A:
    x = 5

a1 = A()
a2 = A()

A.x = 20
print(a1.x, a2.x) #20, 20


#4
class A:
    x = 5

a1 = A()
a2 = A()

a1.x = 50
print(a1.x, a2.x) #50, 5


#5
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.count)