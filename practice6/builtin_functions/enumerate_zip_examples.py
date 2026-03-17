#enumerate(нумерация)
students = ["Ayana", "Amira", "Aziza"]
for i, name in enumerate(students): 
    print(i, name)


#zip
fname = ["Ayana", "Amira", "Aziza"]
lname = ["Shaikhayeslyam", "Kenzhegulova", "Ryskaliyeva"]
for n,a in zip(fname, lname):
    print(n, a)