import shutil
# print(dir(shutil))
import os

shutil.copy("P74.py","P74-A.py")
shutil.copy2("P74.py","P74-A.py")
os.chdir("C:\\Programming")
shutil.copytree("Python","Py")
# os.chdir("C:\\Programming\\Python")
shutil.rmtree("Py")