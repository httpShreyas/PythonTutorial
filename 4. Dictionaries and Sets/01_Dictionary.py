'''Properties of dictionaries in python
    1 It is unordered
    2 It is mutable
    3 It is indexed  
    dictionary = {keys:values}'''

empty_dictionary = {}
marks = {
    "Shreyas": 70,
    "Ritesh": 79,
    "Sandesh": 80

}

print(marks)

print(marks["Sandesh"]) #Prints the corresponding value in the dictionary

'''>When the keys are same, the keys get updated instead of repeating themsselves
    
    
    >When the values are same, they repeat themselves'''

#Checking a key 
if "Raj" in marks : 
    print("true")

#Looping through a dictionary:
for key in marks:
    print(key)

for value in marks.values():
    print(value)

#Copying a dictionary:
new = marks.copy()