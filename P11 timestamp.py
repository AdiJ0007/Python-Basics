import time
timestamp = time.strftime('%H,%M,%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp2 = int(time.strftime('%M'))
print(timestamp)
timestamp3 = int(time.strftime('%S'))
print(timestamp)
if(timestamp > 6 and timestamp < 12):
    print("Good Morning")
elif(timestamp >= 12 and timestamp < 16):
    print("Good Afternoon")
elif(timestamp >= 16 and timestamp < 21):
    print("Good Evening")
elif(timestamp >= 21 and timestamp < 6):
    print("Good Night")
