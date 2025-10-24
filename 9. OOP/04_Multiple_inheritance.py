class A:
    varA = "Welcome to class a"

class B:
    varB = "Welcome to class B "

class C(A, B):
    print("Welcome to class C")

c1 = C()
print(c1.varB , c1.varA)
