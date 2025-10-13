Q = ["Fastest car ever made is","Fastest record for 0-400-0 is held by?","Most expensive car in 2024"]
A1 = ["Koenigsegg Jesko Absolut","Bugatti Bolide","Hennessey Venom F5","Bugatti Chiron Supersport"]
A2 = ["Koenigsegg Regera","Rimac Nevera","Koenigsegg Jesko Absolut","Bugatti Chiron"]
A3 = ["Rolls Royce Boat Tail","Rolls-Royce La Rose Noire Droptail","Bugatti La Voiture Noire","Pagani Zonda HP Barchetta"]
a = 0

print("Chaliye shuru karte hai")
print("Ye rha pehla sawaal aapki screen par")
print("choose the correct option")
print(Q[0])
print(A1)
m = input("\n")

if(m == A1[0]):
    print("Congratulations you have selected the correct option")
    a = a + 1000
    print("Agla sawaal aapki screen par ye rha")
    print(Q[1])
    print(A2)
    n = input("\n")
    
    if(n == A2[2]):
        print("Congratulations you have selected the correct option")
        a = a + 10000
        print("and here's the next question")
        print(Q[2])
        print(A3)
        o = input("\n")
    
        if(o == A3[1]):
            print("Wooow! Congrats!! You Haave won the Toyota Supra Mk4!!!!!!!!")
            a = a + 100000
            print("here is your prize money, $",a)
        else:
            print("sorry you chose the wrong one")
            print("Still you have got Mazda miata")
            print("And a prize money of $",a)
    
    else:
        print("sorry you chose the wrong one")
        print("No problem friend, you have won the prize money of $",a+3000)

else:
    print("sorry you chose the wrong one")
    print("oops!! you won the worst prize :) tesla ;)")