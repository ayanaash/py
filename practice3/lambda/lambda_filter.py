#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#2
nums = [3, 6, 8, 2]
result = list(filter(lambda x: x > 5, nums))
print(result)

#3
nums = [-2, 3, -1, 5]
result = list(filter(lambda x: x > 0, nums))
print(result)

#4
words = ["hi", "hello", "ok", "python"]
result = list(filter(lambda x: len(x) > 3, words))
print(result)

#5
words = ["apple", "banana", "ant", "cat"]
result = list(filter(lambda x: x[0] == "a", words))
print(result)