number = int(input("Enter a number to multiply: "))

i = 1

while i < 12:
    result = i * number
    final = f'{number} x {i} = {result}'
    i += 1
    print(final)
