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
    case _:
        print("You entered wrong input")

