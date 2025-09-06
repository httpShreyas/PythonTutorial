'''
Suppose a is a very long string with emails
emails = []
The data needs to be stored.
It needs to persist and be stored in non volatile memory, which is permanent
'''

f = open("file.txt", "r") 
#Here r means read mode. IT is by default
data = f.read() #Reads the given text file
print(data)
f.close #Closing the file is very important
