a = int(input("Enter the number :"))

# use excepetion handling
try:
    for i in range(1 , 11):
        print(f"the result is int({a}) * {i} = {int(a)*i}")
except:
    print("Sorry! Wrong Input! Please enter the integer number")

print("Important message")
print("Programe terminated")