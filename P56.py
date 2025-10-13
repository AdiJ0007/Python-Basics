import os

print(os.getcwd())
os.chdir("C:\\Programming\\Python\\xavier\\data\\tut 1")
print(os.getcwd())

files = os.listdir("C:\\Programming\\Python\\xavier\\data\\tut 1")
print(files)
i = 1
j = 1
k = 1
for f in files:
    if f.endswith(".pdf"):
        os.rename(f"{f}",f"{i}.pdf")
        i += 1
for f in files:
    if f.endswith(".jpg"):
        os.rename(f"{f}",f"{j}.jpg")
        j += 1
for f in files:
    if f.endswith(".txt"):
        os.rename(f"{f}",f"{k}.txt")
        k += 1
print(files)
# do the same loop for as many types of objects available

# def nchange():
#     s1 = set()
#     for f in files:
#         typ = f[-3:]
#         print(typ)
#         s1.add(typ)
#     print(s1)
# nchange()