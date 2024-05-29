# first of all you import time then print
print("Wellcome!")
import time
tme = time.strftime('%H:%M:%S')
tme1 = time.strftime('%d:%m:%Y')
print("Time : ",tme)
print("Date : ", tme1)
print("\n")

tme2 = time.strftime('%H:%M:%S')
print(tme2)
print(time.strftime('%H'))
print(time.strftime('%M'))
print(time.strftime('%S'))
