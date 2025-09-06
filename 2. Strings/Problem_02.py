#Write a program to detect double space in a string

name = "My name is  shreyas  nambiar  and i am 17 years old"

print(name.find("  "))
#It returns the index of the substring in the parent string

#If it returns -1 , There is no occurence
#IF it returns any other number, there is an occurence

''' Q2: Replace the double space with single spaces'''

print(name.replace("  ", " ")) #This replaces all the occurences in the string


#The original string is not changed by running functions on them, therefore the strings are IMMUTABLE
#Lists are changed
print("Hi")


