#1
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#2
nums = [3, 1, 2]
print(sorted(nums, key=lambda x: x))

#3
words = ["banana", "apple", "cherry"]
sort = (sorted(words, key=lambda x: x))
print(sort)

#4
pairs = [(3, 1), (1, 5), (2, 2)]
print(sorted(pairs, key=lambda x: x[0])) #[(1, 5), (2, 2), (3, 1)]  1st element

#5
pairs = [(3, 1), (1, 5), (2, 2)]
print(sorted(pairs, key=lambda x: x[1])) #[(3, 1), (2, 2), (3, 1)]  2nd element