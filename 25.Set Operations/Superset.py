cities = {"Kotli","Khuiratta","Nakyal","Dungi"}
cities1 = {"Rawalakot","Dungi1","Kotli1","Bagh"}
# superset - > agr cities1 ki values cities mein hain
# to cities superset ha cities1 ka otherwise ni
print(cities.issuperset(cities1))

# yahan par ha
cities2 = {"Kotli","Khuiratta","Nakyal","Dungi"}
cities3 = {"Dungi","Kotli"}
print(cities2.issuperset(cities3))