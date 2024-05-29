# functions
def multiple(a,b):
    print(a*b)

def add(a,b):
    print(a+b)

def gmean(a,b):
    print((a+b)/(a*b))

def lesser(a,b):
    if(a < b):
        print(a," is less than ",b)
    else:
        print(b," is less than ",a)

a = 6
b = 9
multiple(a,b)
add(a,b)
gmean(a,b)
lesser(a,b)
