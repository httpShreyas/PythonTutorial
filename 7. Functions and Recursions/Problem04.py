'''Write a python program that prints the following star pattern:
    ***
    **
    *'''
def func(n):
    for i in range(n,0,-1):
        print("*" * i )

func(100)