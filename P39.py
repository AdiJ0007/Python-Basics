f = open("example.txt",'r')
print(f)
print(f.read())
f.close()

p = open("example2.txt",'w')
p.write("Hey there, I am probably alive...")
p.close()

l = open("example2.txt",'a')
l.write("But maybe not for long.")
l.close()

n = open("example3.txt",'x')
n.write("Lets Enjoy!!!!!")
n.close()

with open("example4",'a') as f:
    f.write("E-N-J-O-Y-!")