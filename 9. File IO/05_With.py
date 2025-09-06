f = open("Myfile.txt")
print(f.read())
f.close()


#The same can be written using with statement like this
with open("Myfile.txt") as f:
    f.read()
#With this, you dont need to close the file explicitly