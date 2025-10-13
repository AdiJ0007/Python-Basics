f = open("example.txt",'r')
i = 0
while True:
    i += 1
    m = f.readline()
    if not m:
        break
    m1 = int(m.split(",")[0])
    m2 = int(m.split(",")[1])
    m3 = int(m.split(",")[2])
    print(f"The marks of student {i} in Mathsis is {m1*5}")
    print(f"The marks of student {i} in Science is {m2*5}")
    print(f"The marks of student {i} in English is {m3*5}\n")
f.close()
   
t = open("example3.txt",'w')
n = ["Yash is probably working...\n","Let me see.\n","Let's check.\n","Ohhh!!!! He's really working!!\n","What a miracle!!\n"]
t.writelines(n)
t.close()
