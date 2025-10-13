name = "Pagani"
country = "Italy"
s1 = "The company {1} is of {0}"
print(s1.format(country,name))
t = "The price of this car is only $ {price:.1f}M"
print(t.format(price = 6.495))

print(f"The company {name} is of {country}")
print(f"We use f-strings like this:The company {{name}} is of {{country}}")
price = 6.495
print(f"The price of this car is only $ {price:.1f}M")
print(f"{7*7}")