import time

t = (time.strftime('%H:%M:%S'))
# print(time)
hour = int(time.strftime('%H'))
hour = int(input("Enter hour : "))
# print(hour)
if(hour>=0 and hour<12):
    print("Good Morning!")
elif(hour>=12 and hour<20):
    print("Good AfterNoon Sir!")
elif(hour>=20 and hour<0):
    print("Good Evening Sir!")    
else:
    print("Thankyou")