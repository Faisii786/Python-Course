# set value ko repeat ho usko print ni krty
# example
# syntax "variable name = {data}""
set1 = {1,2,3,4,5,5,5,6,1,3,2}
print(set1)
print("")

# check set type so we use
faisal = set()  #empty set
print(type(faisal))
print("")

# acces a elemets using for loop not indexing
for value in set1:
    print(value)