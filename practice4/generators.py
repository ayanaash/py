#1
n=int(input())
def my_func(n):
    for i in range(1,n+1):
        yield i*i 

for i in my_func(n):
    print(i)


#2
n=int(input())
def my_func(n):
    for i in range(0,n+1):
        if i%2==0:
            yield i

print(", ".join(str(i) for i in my_func(n)))


#3
n=int(input())
def my_func(n):
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            yield i 

for i in my_func(n):
    print(i)

  

#4
a=int(input())
b=int(input())
def squares(a,b):
    for i in range(a,b+1):
        yield i*i 

for i in squares(a,b):
    print(i)


#5
n=int(input())
def my_func(n):
    for i in range(n,-1,-1):
        yield i 

for i in my_func(n):
    print(i)