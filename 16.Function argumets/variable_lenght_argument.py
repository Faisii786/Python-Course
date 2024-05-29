# Example 1
def average(*numbers):
    print(type(numbers)) # check the type of numbers
    sum= 0
    for i in numbers:
        sum = sum + i
    print("The average is", sum/len(numbers))

average(10,20)