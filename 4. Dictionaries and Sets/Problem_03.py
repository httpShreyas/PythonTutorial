#Create an empty dictionary.Allow 4 people to enter their favourite language as value and use key as their names.Assume their names are unique
#Attempt
'''fav_languages = {}
name = input("Enter your name: ")
language = input("Enter your favourite language: ")

fav_languages.update(name : language)'''

#Answer
fav_languages = {}

for i in range(4):
    name = input("Enter your name: ")
    language= input("Enter your favourite programming language: ")
    fav_languages.update({name:language})

print(fav_languages)


''' Q2: What will happen if the names of two friends are the same
    Attempt: The names will still show up, even if they are duplicaeted
    correct
    
    Q3: What will happen if the languages are similar
    Answer: The languages will get updated'''
