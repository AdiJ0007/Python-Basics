a = (input("Enter a no.: "))
print(f"The table of {a} is :")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
print("Some imp code")
print("End of program")

    
# a = (input("Enter a no.: "))
# print(f"The table of {a} is :")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#     print("Invalid input")
# print("Some imp code")
# print("End of program")

try:
    x = int(input("Enter an integer: "))
    y = [6,4]
    print(y[x])
except ValueError:
    print("The no. entered is not an integer")
except IndexError:
    print("IndexError")
