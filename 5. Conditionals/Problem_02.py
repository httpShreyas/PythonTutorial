#Write a program to detect spam in comments:


p1 = "Buy my course"
p2 = "Youre poor"
p3 = "You need to start making money now"

message = input("Enter your comment here: ")

if p1 or p2 or p3 in message:
    print("Your message contains spam")

else:
    print("Your message does not contain spam: ")