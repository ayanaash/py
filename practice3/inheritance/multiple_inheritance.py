#1
class A:
    x = 5

class B:
    y = 10

class C(A, B):
    pass

c = C()
print(c.x, c.y)   #5, 10


#2
class A:
    def add(self, x):
        return x + 5

class B:
    def add(self, x):
        return x + 10

class C(A, B):
    pass

c = C()
print(c.add(3))  #8 (берем только А потому что метод сначала найден в А)


#3
class A:
    def add(self, x):
        return x + 5

class B:
    def add(self, x):
        return x + 10

class C(A, B):
    def add(self, x):
        return x + 20

c = C()
print(c.add(3))   #23


#4
class A:
    def add(self, x):
        return x + 5

class B:
    def add(self, x):
        return x + 10

class C(A, B):
    def add(self, x):
        return super().add(x) + 2

c = C()
print(c.add(3))   #10 (firstly A, later C)


#5
class A:
    def multiply(self, x):
        return x * 2

class B:
    def add(self, x):
        return x + 3

class C(A, B):
    pass

c = C()
print(c.multiply(5))
print(c.add(5))    #10 \ 8