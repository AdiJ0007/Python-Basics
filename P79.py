import time
from plyer import notification


title = "Health Reminder"
message = "DRINK water"
# timeout = 10

if True:
    notification.notify(title,message,timeout = 10)
    time.sleep(60*2)
    
print("execution complete")