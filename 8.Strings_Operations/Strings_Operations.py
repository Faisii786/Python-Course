name = "Faisal"
print(name)
print("\n")

# Strings are immutable
# its mean original string are not change
# but when we apply a upper case on string
# then it create copy of that strig then operate.
print("We perform uppercase operation")
print(name.upper())
print(name.lower())
print("\n")

# remove ! sign using rstrip at end but not we remove starting
names="Faisal !!!!!!!"
print(names.rstrip("!"))
print("\n")

# replace all string
print(names.replace("Faisal", "Mughal"))

# split : Convert a list
fai = "Faisal !!!! Aslam!! Universityof!! Poonch"
print(fai.split(" "))
print("\n")

# capatilize : turn first letter capital and others all in small
intr = "faisal faisal asMaM !!!"
print(intr.capitalize())
print("\n")

# center
print(intr.center(50))
print("\n")

#count
print(intr.count("faisal"))
print("\n")

#end swith : kya meri string given value sy end ho rhi ha ?
print(intr.endswith("!"))
print("\n")

#  find : return index number : other return -1
intr = "faisal faisal asMaM !!!"
print(intr.find("asM"))
print("\n")

#  find : return index number : other return error
intr = "faisal faisal asMaM !!!"
print(intr.find("asM"))
print("\n")

#  isaplhanumber : is string alphanumeric or not mean (AtoZ atoz) 0to9 return true or false
intr = "WellcomeToMyPage"
print(intr.isalnum())
print("\n")

#  isaplhanumber : is string alphanumeric or not mean (AtoZ atoz) return true or false
intr = "WellcomeToMyPage"
print(intr.isalpha())
print("\n")

#  islower : is string lower case or not mean : return true or false
intr = "WellcomeToMyPage"
print(intr.islower())
print("\n")

#  printable : \n -> not printable : return true or false
intr = "WellcomeToMyPage\n"
print(intr.isprintable())
print("\n")

#  istitle :: return true or false
intr = "WellcomeToMyPage"
print(intr.istitle())
print("\n")

#  startwith :: return true or false
intr = "WellcomeToMyPage"
print(intr.startswith("Well"))
print("\n")

#  swapcase :convert lower to upper and upper to lower
intr = "WellcomeToMyPage"
print(intr.swapcase())
print("\n")

#  title :convert title/upper case all words first letter
intr = "wellcome to my page"
print(intr.title())
print("\n")
