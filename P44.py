a = [1,3,5]
b = [1,3]
print(a is b)
print(a == b)

a = [1,2]
b = [1,2]
print(a is b) #checks memory location of objects
print(a == b) #checks value of objects


a = {1,2}
b = {1,2}
print(a is b)
print(a == b)

a = 4
b = 4
print(a is b)
print(a == b)

a = "Yash"
b = "Yash"
print(a is b)
print(a == b)

a = {1:3,2:4}
b = {1:3,2:4}
print(a is b)
print(a == b)