import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
h = int(time.strftime('%H'))
if(h>=3 and h<12):
    print("Good Morning Sir")
elif(h>=12 and h<16):
    print("Good Afternoon Sir")
elif(h>=16 and h<21):
    print("Good Evening Sir")
else:
    print("Good Night Sir")