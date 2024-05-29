cities = {"Kotli","Khuiratta","Nakyal","Dungi"}
# print(cities)
cities1 = {"Rawalakot","Dungi","Kotli","Bagh"}
# intersection - > common values ko print krta ha
print(cities.intersection(cities1))
# update - > update kr do set 1 ko
cities.intersection_update(cities1)
print(cities)
