import random

def Play_game():
    CC = ["S","W","G"]
    C = input("Chose: S->Snake, W->Water, G->Gun : ")
    if C not in CC:
        raise SyntaxError("Enter valid choice")
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

    print(f"The pc chose {PC} and you chose {C}")
    print(Game(C,PC))
    
    play_again = int(input("Enter 1 to play again and 2 to exit: "))
    if(play_again == 1):
        Play_game()
    else:
        print("Heh! Scared of losing!")

Play_game()