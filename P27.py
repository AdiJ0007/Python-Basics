dic = {"Jdm":"RX-7","Sports":"Cayman S","Muscle":"Mustang","Gasoline":True,"Best":10}
print(dic)

print(dic["Jdm"])
print(dic["Muscle"])
print(dic.get("Sports"))

print(dic.values())
print(dic.keys())
for key in dic.keys():
    print(key)
for key in dic.keys():
    print(f"The value corresponding to the key {key} is {dic[key]}")
    
print(dic.items())
for key, value in dic.items():
    print(f"The value corresponding to the key {key} is {value}")

dic["Muscle"] = "Camaro"

print(dic.items())
for key, value in dic.items():
    print(f"The value corresponding to the key {key} is {value}")
    
# print(dic["Hyper"]