import time

def usingwhile():
    i = 0
    while i<50:
        i = i + 1
        print(i)

def usingfor():
    for i in range(50):
        print(i)

init = time.time()
print(init)
usingwhile()
print(time.time() - init)
usingfor()
print(time.time() - init)

print(4)
time.sleep(3)
print(time.time() - init)
print("This is printed after 3 seconds")

t = time.localtime()
format_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(format_time)