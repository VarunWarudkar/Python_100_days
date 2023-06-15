'''
Write a program to clear the clutter inside a folder on your computer. 
You should use os module to rename all the png images from 
1.png all the way till n.png where n is the number of png files in that folder. 
Do the same for other file formats. For example:

sfdsf.png --> 1.png
vfsf.png --> 2.png
this.png --> 3.png
design.png --> 4.png
name.png --> 5.png
'''
import os

def os_changeName(idx_itom):
    index,itom = idx_itom
    ext = itom.split(".")[1]
    ext1 = "." + str(ext)
    print(f"index is {index} and ext is {ext1}")
    return  str(index + 1) + ext1

def os_rename(a,b):
    os.rename(a,b)

path = os.getcwd()+"\\txt"

old_path = os.getcwd()
os.chdir(path=path)
x = os.listdir()
y = list(map(os_changeName, enumerate(x)))
for (a,b) in zip(x,y):
   if a.endswith(".txt"):
      os_rename(a,b)
list = os.listdir()
print(list)
