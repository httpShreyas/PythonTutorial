'''Write a program to print the star pattern as shown below: 
      *
     ***
    ***** for n = 3'''


n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" " * (n-i) , end= "")
    print("*" * (2*i-1) , end= "")
    print("")


''' 
EXPLANATION: 
n = 3, so three lines are printed.
 1st print line: Star is printed n-i times:
end = "": This cmd is used to prevent the print statement from giving a new line
 '''