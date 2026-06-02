import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
if timestamp < 12:
    print("Good morning!")
elif timestamp > 12 and timestamp < 19:
    print("Good afternoon!")
else:
    print("Good evening!")