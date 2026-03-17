with open('pyt.txt', "a") as f:
  f.write("hii")  

#read the file after the app
with open('pyt.txt') as f:
  print(f.read())