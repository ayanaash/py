#1
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)   #0, 1, 2, 4
    
#2
i = 0
while i < 6:
    i += 1
    if i % 2 == 0:
        continue
    print(i)   #1, 3, 5
    
#3
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print("Hello")   #hello * 4

#4
i = 0
while i < 5:
    i += 1
    if i == 4:
        continue
    print(i * 2)   #2, 4, 6, 10
    
#5
i = 0
while i < 3:
    i += 1
    if i == 2:
        continue
    print("Go")   #go*2