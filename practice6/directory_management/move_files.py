import shutil
import os

os.makedirs("newfolder") #create

if os.path.exists("base.txt"):
    shutil.move("base.txt", "newfolder/base.txt") #moves file to folder
    print("Moved")