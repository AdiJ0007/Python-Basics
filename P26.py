s1 = {1,3,5,6,7}
s2 = {2,4,6,8,3,9}
s3 = {1,3,5,6,7}
s4 = {1,3,4,2,6,4,45}
s5 = {23,5,3,7,38,4}
print(s1,s2,s3,s4,s5)

print(s1.union(s2))
s1.update(s2)
print(s1)

print(s3.intersection(s2))
s3.intersection_update(s2)
print(s3)

print(s4.symmetric_difference(s2))
s4.symmetric_difference_update(s2)
print(s4)

print(s5.difference(s2))
s5.difference_update(s2)
print(s5)

print(s4.isdisjoint(s5))

print(s1.issuperset(s2))

print(s1.issubset(s2))

s3.add(7)
print(s3)

s1.remove(7)
print(s1)
s1.discard(6)
print(s1)

a = s1.pop()
print(s1,a)

del s5
# print(s5)

s4.clear()
print(s4)

if 3 in s1:
    print("present")
else:
    print("absent")