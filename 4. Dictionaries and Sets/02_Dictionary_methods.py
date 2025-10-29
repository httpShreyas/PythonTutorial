
marks = {
    "Shreyas": 70,
    "Ritesh": 79,
    "Sandesh": 80

}
#Adding a pair: 
marks["Raj"] = 43
marks.keys()  #eg Shreyas

marks.values()   #eg 70

marks.update({"Shreyas": 100, "sudarshan": 100})  #Use curled brackets for dictionaries
#Can also be used to add new keys and values


#(marks.get["Shreyas2"]) #Prints none
# (marks["shreyas2"]) #Gives an error

(marks.get('sandesh'))