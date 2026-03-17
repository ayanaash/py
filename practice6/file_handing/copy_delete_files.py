import shutil
import os

shutil.copy("pyt.txt", "new.txt")  #copy pyt and creates new
print("copied")

if os.path.exists("new.txt"):
    os.remove("new.txt")    #delete
    print("eleted")