def goodday(name, ending):
    print(f'Good day {name}')
    return "okay" #Whatever value is assigned to the return value, it will assign it.


a = goodday("Shreyas", "Thanks")
b = goodday("Harry", "Thankyou")

print(a)
print(b)

#Arbitraty arguments 
def arb(*name):
    print("The name of the student is: ", name[0])

arb("shreyas", "sandesh")



#KEYWORD ARGUMENTS 
def keyword(child3, child2, child1):
    print("The youngest child is ", child1)

keyword(child1="shreyas", child2="Sudarshan", child3= "raj") 