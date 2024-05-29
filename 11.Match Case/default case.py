x = int(input("Enter the value of x : "))
# match is use like switch case statement
match x:
    case 0:
        print("x is 0")
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")

    # _ is used for default
    case _ if x>50 and x<80:
        print(x, "is greater than 50")
    case _ if x > 80 and x<=100:
        print(x, "is greater than 80")
    case _:
        print(x,"is greater than 100")