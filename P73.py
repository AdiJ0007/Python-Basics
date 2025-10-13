no = [1,2,3,4,5]
while(n:=len(no))>0:
    print(no.pop())

happy = False
print(happy)

print(happy:= True)

# foods = []
# while True:
#     food = input("What food do you like: ")
#     if(food == "quit"):
#         break
#     foods.append(food)
    
foods = []
while(food:=input("What food do you like: ")!= "quit"):
    foods.append(food)