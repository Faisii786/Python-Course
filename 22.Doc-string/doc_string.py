''' doc mean documented string
always used within function
when we write function name then next line we write 
doc string 
and we also print doc string
it it same as comments
'''

# create a function
def square(n):
    '''Takes a number
and return the square of n '''
    print(n**2)

square(5)
print(square.__doc__)    