name = "Shreyas"
#The counting of characters in any language starts with 0
#Example: 's' is the 0th character


''' The last s is the -1st character 
    The a is the -2nd character of the string
    '''
nameshort = name[0:3] #Start from index 0 all the way till 3 excluding 3
character1 = name[1]


#Negative Slicing

print(name[-1:-4]) #To solve, convert to the corresponding positive index!

print(name[4:1])

print(name[:4]) #Is same as print(name[0:4])

print(name[1:]) #Is same as prirnt(name[1:5])


#Slicing with skip values

word = "Amazing"

print(word[1:6:2]) #gives output <mzn>
#The third number indicates the number of steps

'''PROPERTIES OF A STRING
IMMUTABLE: cannot be changed after creation, returns copies while running funcions on it
ORDERED: Are Indexed
ITERABLE: can loop over characters
'''