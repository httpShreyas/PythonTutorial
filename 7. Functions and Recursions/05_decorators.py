#Decorator takes another function as an argument and enhances the functionality.

def startend_decorator(func):
    def wrapper():
        print("Function start")
        func()
        print("Function end")
    return wrapper
    

#Always return the decorator inside the first code block OR it causes a nonetype error 
@startend_decorator
def print_name():
    print("Shreyas")
    
#Another way to write it: print_name = startend_decorator(print name)




print_name()