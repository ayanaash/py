from functools import reduce

nums = [1,2,3,4,5]

#map
square = list(map(lambda x: x*x, nums))
print(square)


#filter
even = list(filter(lambda x: x%2==0, nums))
print("Filter:", even)


#reduce
sum = reduce(lambda a,b: a+b, nums)
print(sum) #15
 #1+2=3
 #3+3=6
 #6+4=10
 #10+5=15