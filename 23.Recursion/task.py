# fabonacci sequenece

f = 5
def fabonacci(n):
    if(f==0):
        return 0
    elif(f==1):
        return 1
    else:
        return f(n-1) + f(n-2) 

print(fabonacci(6))               