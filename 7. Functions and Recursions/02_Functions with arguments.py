def goodday(name, ending):
    print(f'Good day {name}')
    return "okay" #Whatever value is assigned to the return value, it will return it.



a = goodday("Shreyas", "Thanks")
b = goodday("Harry", "Thankyou")

print(a)
print(b)

#Arbitraty arguments 
#Any number of positional arguments can be passed, the arguments are packed into a tuple 


def arb(*nums):
    print(nums)

arb(2,22,24,1,4,3,2)

#KEYWORD arguments: Any no of arguments can be passed, packed into a dictionary

def kwarg(**Grade):
    print(Grade)


kwarg(a = 90, b=80, c =70 , d =50)