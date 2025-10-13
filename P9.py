s1 = "Mercedes-Benz SLR Mclaren,SLR Mclaren"
s2 = "!!! GTRRRRR !! !!!!!"
s3 = "12stutututu"
s4 = "Maybach"
s5 = "3,2,1 let's go"
s6 = "Mercedes has multiple classes\nS,A,B,C,E,G,AMG"
s7 = "          "


# upper()
print(s1.upper())

# lower()
print(s1.lower())

# rstrip()
print(s2.rstrip("!"))

# replace()
print(s1.replace("SLR Mclaren", "SLS AMG"))

# split()
print(s1.split(" "))
print(s2.split(" "))

# capitalize()
print(s1.capitalize())

# center()
print(s1.center(77))
print(len(s1))
print(len(s1.center(77)))

# count()
print(s1.count("c"))

# endswith()
print(s1.endswith("ren"))
print(s1.endswith("SLR"))
print(s1.endswith("SLR",14,17))

# find()
print(s1.find("Mc"))
print(s1.find("Mcc"))

# index()
print(s1.index("SLR"))
# print(s1.index("SLL"))      commented as it gives an exception

# isalnum()
print(s3.isalnum())
print(s5.isalnum())

# isalpha()
print(s3.isalpha())
print(s4.isalpha())
print(s5.isalpha())

# islower()
print(s3.islower())

# isprintable()
print(s5.isprintable())
print(s6.isprintable())

# isspace()
print(s7.isspace())

# istitle()
print(s4.istitle())

# isupper()
print(s2.isupper())

# startswith
print(s2.startswith("!"))

# swapcase()
print(s1.swapcase())

# title()
print(s6.title())