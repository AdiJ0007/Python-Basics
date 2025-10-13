l = [1,6,2,8,2,0,2,9,6,4,3]
l1 = [23,56,1267,2,89,32,23]
# sort()
# ascending order
l.sort()
print(l)
# reverse order or descending order
l.sort(reverse = True)
print(l)

# reverse()
l1.reverse()
print(l1)

# index()
print(l1.index(2))

# count()
print(l1.count(23))

# copy()
l2 = l1      # this cannot be used as just the reference name is changed,
             # if changes are made, original list is altered
l2 = l1.copy()
print(l2)

# append()
l2.append(7)
print(l2)

# insert()
l2.insert(3,"Cadillac")
print(l2)

# extend()
l3 = [100,200,300]
l2.extend(l3)
print(l2)

# concatenation
l4 = l1 + l2
print(l4)
