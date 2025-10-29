list1 = ["apple","banana", False, 23,23.4, "Shreyas"]

list2 = list() #Gets an empty list 
print(list1[0])   #Prints the element with index 0

list1[0] = "Grapes" #Original list is changed
#Unlike strings, lists are mutable

print(list1[1:4]) #1st included, 2nd arg isnt 
# list1[::1] The third argument is an optional step argument Specifying -1 reverses the list 



list3 = [0] * 6 #Makes a list by repeating the spcified element



#Concatenation: Strings can be concatenated by the + operator 

#List comprehension: 
a = [1,2,3,4,5,6,7,8]
b = [i * i for i in a ]
print(b)