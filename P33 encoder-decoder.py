n = int(input("Enter 1 if you want to encode a word and 2 if you want to decode a word: "))

def rev(x):
    a = ""
    for i in x:
        a = i + a
    return a

def rev1(x):
    l = x[::-1]
    return l

def encoder(p):
    m = p.split(" ")
    n = []
    for w in m:
        if(len(w)>=3):
            r1 = "qwe"
            r2 = "asd"
            a = r1 + w[1:] + w[0] + r2
            n.append(a)
        else:
            n.append(w[::-1])
    j = (" ".join(n))
    return j

def decoder(l):
    m = l.split(" ")
    n = []
    for w in m:
        if(len(w)>=3):
            w = w.removeprefix("qwe")
            w = w.removesuffix("asd")
            a = w[-1] + w[:-1]
            n.append(a)
        else:
            n.append(rev(w))
    j = (" ".join(n))
    return j
            

if(n == 1):
    b = input("Enter a word to be encoded: ")
    print(encoder(b))

elif(n == 2):
    a = input("Enter a word to br decoded: ")
    print(decoder(a))
else:
    raise ValueError("Please enter a valid selection")


    

