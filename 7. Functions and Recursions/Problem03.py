'''Question: Write a function that calculates the sum of first n natural numbers
   Use recursions'''

'''sum(n) = 1 + 2 + ..... + n
   sum(n) = sum(n-1) = n '''

def sum(n):
    if n == 1:
       return 1 
    return sum(n-1) +  n 


print(sum(5))