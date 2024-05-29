# append() method add the value of the last idex
list = [1,2,3,4,4,5,6,7,8]
print(list)
list.append(15)
print(list)
print("")

# sort() method makes your list in assending order
list1 = [10,5,20,59.45,55]
print(list1)
list1.sort()
print(list1)
print("")

# reverse() method makes your list in reverse order
list1 = [1,2,3,4,4,5,6,7,8]
print(list1)
list1.reverse()
print(list1)
print("")

# this method makes your list in dessending order
list1 = [10,5,20,59.45,55]
print(list1)
list1.sort(reverse=True)
print(list1)
print("")


# extend() method extend or cancatenate two lists
list3 = [10,5,20,59.45,55]
print(list3)
list4= [1,2,3,4,5,6]
print(list4)
list3.extend(list4)
print("After cancatenation : ",list3)
print("")
# second method
k = list3 + list4
print(k)
print("")

# copy() method makes your list one time copied
list1 = [1,2,3,4,4,5,6,7,8]
print(list1)
cop = list1.copy()
print(cop)
print("")

# index() method tell the value of the index
list1 = [1,2,3,4,4,5,6,7,8]
print(list1)
print(list1.index(3))
print("")

# count() method count the values that repeat.
list1 = [1,2,2,3,4,2,4,5,6,2,7,8]
print(list1)
print(list1.count(2))
print("")