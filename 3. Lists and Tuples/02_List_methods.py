lst = ["apple","apple","banana","banana","banana", False, 23,23.4, "Shreyas", "Rohan"]

lst.append("3")

#Adds the given item at the end of the list.

lst.extend([3,4,5,6])

#This is used to add multiple items to a list

lst.insert(3,"cherry")

#Inserts the item at a given index, Note: always specify the index first then the item

lst.remove("cherry") #This removes the object specified

#This removes the first occurence of the specified item

lst.pop(5)

#It returns the removed item

print(lst.count("banana"))
#Counts all occurences 

rev_lst = lst.reverse()
print(rev_lst)
#Reverses

#lst.sort() is used to sort a list of numbers. It changes the original list 

#new = lst.sorted(): makes a new list that is sorted..

#LIST SLICING 
sliced_lst = lst[1 : 5]
print(sliced_lst)
