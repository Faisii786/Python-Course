# acces any string
name = "Faisal,Waleed,Soban"
print(name[0:6])  #slicing

# calculate lenght of string
print(len(name))
print("\n")

print("University name")
uname ="upr"
lenght = len(uname)
print(lenght)
print(uname[0:2])
# python automatically understood the starting index. mean 0;
print(uname[:3])
print("\n")

print("Detail")
na = "FaisalMughal"
print(na)
print(len(na))
print(na[0:-3])   #negative slicing
print(na[-5:-3])
print("\n")

# Quick quiz
nm = "harry"
print(nm[-4:-2])
print("\n")

# Practice
names = "FaisalAslam"
print(names[-5:-3])
print("\n")
# 11-5 = 6  / 11-3 = 8
# its mean print 6 to 8 tak words and 8 is not iclude because of n-1

# Another Question
nav = "Proffesional"
print(nav[-4:-1])
