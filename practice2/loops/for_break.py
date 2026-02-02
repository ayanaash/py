#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break    #apple, banana

#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)   #apple
  
#3
for i in range(1, 6):
    if i == 3:
        break
    print(i)   #1, 2
    
#4
for i in range(1, 10):
    if i > 4:
        break
    print(i)    #1, 2, 3, 4

#5
numbers = [1, 3, 5, 6, 7]
for n in numbers:
    if n % 2 == 0:
        print(n)
        break  #6
    
#6
for letter in "abcdef":
    if letter == 'c':
        break
    print(letter)  #a, b