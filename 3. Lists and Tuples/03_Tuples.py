a = (1,45,342,3424,False,"Rohan","Shivam")
#Parentheses are optional 
b = (a,) #this wont return the type as str

print(type(a))
#Tuples cannot be changed. Immutable

item = a[-1] #The second last item

#mylist2 = list(my_tuple) #converts the tuple into a list and returns a copy 

a[2:5] #Last index not included
#Slicing similar to that of a list.

#Unpacking 
c = "Shreyas", 18, "mumbai"
name, age, city = c 
#Assigns the elements 

d = (0,4,6,7,8)
i1, *i2, i3 = d
#Returns a list of the * variable

