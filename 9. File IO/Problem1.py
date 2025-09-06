'''
Q1 Write a program to read the text from given file poems.txt and find out if it contains the word twinkle'''


f = open("poem.txt")

c = f.read()
if "twinkle" in c:
    print("Word is present")

else:
    print("Word is not present")

f.close()