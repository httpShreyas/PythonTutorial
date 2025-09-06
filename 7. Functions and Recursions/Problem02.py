#Write a function to convert celsius into farenheit:

def converter(c):
    f = (9/5 * c ) + 32
    return f 

ans1 = converter(100)
print(ans1)


def converter2(f):
    c = (5/9) * (f - 32)
    return c 
ans2 = round(converter2(100))
print(ans2)


#The round function rounds up the float to the nearest integer.7
#The end in print function is used to prevent new line
