# only vapils for python 3.10
x = int(input("Chose from the no.(1,2,3,4,5): "))
match x:
    case 1:
        print("You Chose 1")
    case 2:
        print("You Chose 2")
    case 3:
        print("You Chose 3")
    case 4:
        print("You Chose 4")
    case 5:
        print("You Chose 5")
    case _:
        print("Invalid choice")