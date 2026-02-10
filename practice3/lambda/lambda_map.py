#1
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#2
nums = [1, 2, 3, 4]
sq = list(map(lambda x : x * x, nums))
print(sq)

#3
nums = [1, 2, 3, 4]
result = list(map(lambda x: x % 2 == 0, nums))
print(result)

#4
words = ["hi", "python", "ok"]
result = list(map(lambda x: len(x), words))
print(result)  # 2, 6, 2

#5
a = [1, 2, 3]
b = [4, 5, 6]
result = list(map(lambda x, y: x + y, a, b))
print(result)  # 5, 7, 9