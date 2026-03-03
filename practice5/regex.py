#1
import re
s = input()
if re.fullmatch(r'ab*', s):
    print("Match")
else:
    print("No match")
    
#2
import re
s = input()
if re.fullmatch(r'ab{2,3}', s):
    print("Match")
else:
    print("No match")
    
#3
import re
s = input()
matches = re.findall(r'[a-z]+_[a-z]+', s)
print(matches)  #python

#4
import re
s = input()
matches = re.findall(r'[A-Z][a-z]+', s)
print(matches)  #Python

#5
import re
s = input()
if re.fullmatch(r'a.*b', s):  #whatever between 'a' and 'b'
    print("Match")
else:
    print("No match")
    
#6
import re
s = input()
snew = re.sub(r'[ ,.]', ':', s) #replace w :
print("Result:", snew)

#7
import re
s=input()
print(re.sub(r'_([a-z])', lambda m:m.group(1).upper(), s)) #py_thon -> pyThon

#8
import re
s = input()
parts = re.split(r'(?=[A-Z])', s)
print("Split parts:", parts)  #HelloWorld -> 'Hello', 'World'

#9
import re
s = input()
result = re.sub(r'([A-Z])', r' \1', s).lstrip()
print(result)   #HelloWorld -> Hello World

#10
import re
s = input()
snake = re.sub(r'([A-Z])', r'_\1', s).lower()
print(snake)   #helloWorld -> hello_world