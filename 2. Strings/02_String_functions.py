name = " Shreyas nambiar "

print(len(name)) 
#Gives the number of characters present in a word

print(name.endswith("yas"))
#Checks if the string ends with (a particular argument)

print(name.startswith("shr")) 
#False because the function is case sensitive

print(name.capitalize())
 #capitalizes the first letter of the string 

print(name.title()) 
#Capitalizes the first letter of each word

print(name.strip()) 
# Strips the string of all the whitespaces

print(name.split(" ")) 
#Splits the elements of the string into a list according to the given argument

print(name.replace("r","a"))
#Replaces the first argument provided with the second argument

print(name.find("r"))
#Gives the first index of the substring

print(name.count("a"))
#Counts all the occurences

print(name.isdigit())
#Checks if there is a number in the string
