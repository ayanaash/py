#1
import math
degree = float(input())
radian = degree * math.pi/180
print(radian)


#2
import math
h = float(input())
a = float(input())
b = float(input())

area=(a+b)/2 * h
print(area)


#3
import math
n=int(input())
s=float(input())
area=(n*s*s)/(4*math.tan(math.pi/n))
print("Area of the pol: ",area)



#4
a = float(input())
h = float(input())
area = a*h
print(area)
