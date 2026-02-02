#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
#2
for x in "banana":
  print(x)  

#3
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)    #red apple, red banana, red cherry, big apple...
    
#4
for x in range(6):
  print(x)  #0, 1, 2, 3, 4, 5
  
#5
for x in range(2, 30, 3):
  print(x)    #2, 5, 8, ... , 26, 29