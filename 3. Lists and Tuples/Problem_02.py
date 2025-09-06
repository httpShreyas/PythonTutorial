#Write a program to accept the marks of 6 students and sort them into a list

f1 = int(input("Enter the marks of student 1: "))
f2 = int(input("Enter the marks of student 2: "))  
f3 = int(input("Enter the marks of student 3: "))
f4 = int(input("Enter the marks of student 4: "))
f5 = int(input("Enter the marks of student 5: "))
f6 = int(input("Enter the marks of student 6: "))

marks = [f1, f2, f3, f4, f5, f6]
marks.sort()
print(marks)
