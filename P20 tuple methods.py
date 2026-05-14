tp1 = (1,6,8,9,87,"Chiron",False)
l1 = list(tp1)
l1.append("Veyron")
print(l1)
l1.pop(4)
print(l1)
l1[3] = "Divo"
print(l1)
tp1 = tuple(l1)
print(tp1)

tp2 = ("Agera r","Regera","Gemera","jesko absolut","ccx","ccxr","one:1")
tp3 = tp1+tp2
print(tp3)

c = tp2.count("one:1")
print(c)

i = tp2.index("Agera r")
print(i)
i1 = tp1.index(6,1,3)
print(i1)

