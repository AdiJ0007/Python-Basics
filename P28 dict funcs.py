info = {"Supra" : "2JZ","Skyline" : "Inline 6","Carrera GT" : "V10"}
dat = {247:32,395:68,777:69,707:69}
dat1 = {203:32.4,297:78}

dat.update(dat1)
print(dat)

dat1.clear()
print(dat1)

dat.pop(707)
print(dat)

dat.popitem()
print(dat)
