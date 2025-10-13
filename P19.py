tp = (1,3,5,6,"saleen",True)
print(type(tp),tp)
tp1 = (1,)
print(tp1)
# tp[0] = 34      #commented as this gives an error
print(tp[0])
print(tp[1])
print(tp[2])
print(tp[3])
print(tp[-4])
if 3 in tp:
    print("yes present in tp")