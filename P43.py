def cube(x):
    return x*x*x
print(cube(2))

def fil(p):
    return p>10

def avg(x,y):
    return (x+y)/2

l1 = [1,2,4,6,8,4,2]
n = []
for i in l1:
    n.append(cube(i))
print(n)

nl = list(map(lambda x: x*x*x,l1)) #previously was nl =  list(map(cube,l1))
# this is to show that this can accept a lambda function
print(nl)

no = list(filter(lambda p: p>10,nl)) #previously was no = list(filter(fil,nl))
print(no)

from functools import reduce
z = reduce(lambda x,y: (x+y)/2,l1) #previously was z = reduce(avg,l1)
print(z)