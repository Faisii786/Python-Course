# Example 1
def average(a=5,b=10):
    print("The average is",(a+b)/2)

average()
# second method is
# in this time pyhton ignore function paramater
# and include the value of below parameters which is called
average(a=21,b=9)

#Example 2
def name(fname,lname="Aslam"):
    print("Hello",fname,lname)

name(fname="Faisal")
# or
# name("faisal")