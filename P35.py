l1 = [12,46,34,6734,76,347,354,45]
# x = 0
# for i in l1:
#     print(x,i)
#     if(x == 4):
#         print("Great!!!")
#     x += 1

for i,x in enumerate(l1):
    print(i,x)
    if(i == 4):
        print("Great!!!")
print("\n")
for i,x in enumerate(l1,start = 1):
    print(i,x)
    if(i == 4):
        print("Great!!!")