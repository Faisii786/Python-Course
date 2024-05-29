# we store multiple items with its specific key
# syntax

dic ={
    15: "Faisal",
    16: "Soban",
    5: "Waleed",
    4: "Hamza",
    47: "Saad",
}
# if we all values then use
print(dic)
print("")

# if we acces specific then
print(dic[47])
print("")

# if we print only keys then use
print(dic.keys())
print("")

# if we print only values then use
print(dic.values())
print("")

# if we print item type
print(dic.items())
print("")

for key in dic.keys():
    print(f"The value of {key} against {dic[key]} ")
