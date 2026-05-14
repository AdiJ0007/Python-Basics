marks = [35,47,32,45,49]
print(marks)
print(type(marks))
# printing particular item from list
print(marks[0])
print(marks[1])
print(marks[2])

#  negative indexing
score = [12,34,67,"El camino",True]
print(score[-3])
print(score[len(score)-3])
print(score[5-3])
print(score[2])

# searching in list
if 67 in score:
    print(True)
else:
    print(False)
# if "67" in score:
#    print(True)
# else:
#    print(False)  
# same thing applies for string

# slicing of list
print(score[1:4])

# list comprehension
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2 == 0]
print(lst)
