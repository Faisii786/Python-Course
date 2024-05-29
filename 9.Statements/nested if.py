age = int(input("Enter you age : "))
if(age<18):
    print("Your age is less than 18")
elif(age>=19):
    print("Your age is greater than 18")
    if(age>=20 and age<=30):
        print("Your age is between 20 to 30")
    elif(age >= 31 and age <= 40):
        print("Your age is between 31 to 40")
    else:
        print("Your age is upto 40")
else:
    print("Happy")