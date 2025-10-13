def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hell():
    print("Hello Ladies")

@greet
def add(a,b):
    print(a+b)

hell()
add(13,46)