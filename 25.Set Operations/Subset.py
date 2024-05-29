cities = {"Kotli","Khuiratta","Nakyal","Dungi"}
cities1 = {"Rawalakot","Dungi1","Kotli1","Bagh"}
# subset - > agr cities1 ki values cities mein hain
# to cities1 subset ha cities ka otherwise ni ha
print(cities1.issubset(cities))

# yahan par ha
cities2 = {"Kotli","Khuiratta","Nakyal","Dungi"}
cities3 = {"Dungi","Kotli"}
print(cities3.issubset(cities2))