f = open("example2.txt",'r')
f.seek(10)
print(f.read(10))
print(f.tell())
f.close()

with open("example5.txt",'w') as f:
    f.write("Hello World")
    f.truncate(5)
with open("example5.txt",'r') as f:
    print(f.read())