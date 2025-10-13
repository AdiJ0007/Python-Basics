for i in range(5):
    print(i)
else:
    print("Succesfully completed the loop")
    
for i in range(6):
    print(i)
    if(i == 4):
        break
else:
    print("Succesfully completed the loop")
    
for i in range(10):
    x = i+1
    print(f"iteration no. {x} in the loop")
else:
    print("this is the else block")
    print("loop succesfully completed")
print("out of the loop")

i = 0
while (i<7):
    i = i+1
    print(i)
    if(i==5):
        break
else:
    print("Completed")