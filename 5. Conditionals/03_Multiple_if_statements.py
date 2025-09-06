a = int(input("Enter your age"))

#If statement 1

if a % 2 == 0:
    print("Number is divisible by 2")
#End of if statement 1

#If statement 2
if a >= 18:
    print("You are above the age of consent")

elif a < 0:
    print("You cannot enter a negative age")

else:
    print("You are below the age of consent")
#End of if statement 2


'''Both if statements work seperately, if the conditions match, both will get executed'''