myString = "Yep, this is a string, indeed!"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? ")
print("Beautiful name " + str(name))

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))
print("%s, you like a %s %s!" % (name,color,animal))