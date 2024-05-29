list = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66]
print("Simple Method")
print(list)
print("")

print("Print by indexing")
print(list[:]) # automatically enter this 0:len(list)
print("")

print("Print by possitive indexing")
print(list[1:7])
print("")

print("Print by negative indexing")
print(list[1:-6]) # first convert in possitive indexing
print("")

print("Third Paramater jumping")
print(list[0:9:2]) # :2 mean 2 numbers py aga jump kr ky 2sra wala print kr dy ga