f = open("Myfile.txt", "r")

lines = f.readlines()
#This returns each line as a list element
print(lines, type(lines))
f.close()

line1 = f.readline()
print(line1, type(line1))  #This will read and print next line
#using while loops
line = f.readline()
while line != "":
    print(lines)
'''
line2 = f.readline()
and vice versa
'''