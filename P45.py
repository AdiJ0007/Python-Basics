import random

CC = ["S","W","G"]
C = input("Chose: S->Snake, W->Water, G->Gun : ")
if (C=="S" or C=="W" or C=="G"):
    pass
else:
    raise SyntaxError("Enter valid choice")
points = 0
PC = random.choice(CC)

def Game(C,PC):
    points = 0
    "S" > "W"
    "G" > "S"
    "W" > "G"
    if(C>PC):
        print("you won")
        points = points + 1
    elif(C==PC):
        print("Its a draw")
    else:
        print("you lose")
        points = points-1
    return points

def con(a):
    if (a == 1):
        C = input("Chose: S->Snake, W->Water, G->Gun : ")
        PC = random.choice(CC)
        Game(C,PC)
        a = int(input("do you want to continue(1 for yes and 2 for no): "))
        return con(a)
    else:
        print(f"Your total points are {points}")

print(f"The pc chose {PC} and you chose {C}")
print(Game(C,PC))
a = int(input("do you want to continue(1 for yes and 2 for no): "))
con(a)