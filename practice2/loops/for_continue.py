#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)   #apple, cherry
  
#2
for i in range(1, 6):
    if i == 3:
        continue
    print(i)   #1, 2, 4, 5
    
#3
for letter in "abcde":
    if letter == 'b':
        continue
    print(letter)  #a, c, d, e
    
#4
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)   #1, 3, 5
    
#5
for i in range(1, 9):
    if i == 5 or i == 7:
        continue
    print(i)   #1, 2, 3, 4, 6, 8 