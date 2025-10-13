# def double(x):
#     return x*2
double = lambda x : x*2
avg = lambda x,y: (x+y)/2

print(double(5))
print(avg(4,6))

def apl(p,n):
    s = 7 + p(n)
    return s
print(apl(lambda x: x*x,3))