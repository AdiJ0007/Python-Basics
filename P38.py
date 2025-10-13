x = 4
print(x)
y = 12
print(y)

def gen():
    x = 10
    print(x)
    global y
    y = 3

gen()
print(y)