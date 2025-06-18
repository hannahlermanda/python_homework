#Task 2: A Decorator that Takes an Argument

#Declare a decorator called type_converter
#Has one argument called type_of_output
def type_converter(type_of_output):

    def type_converter_decorator(func):
        def type_converter_wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            #Convert the return from func to the corresponding type
            return type_of_output(x)
        return type_converter_wrapper
    return type_converter_decorator

#Pass str as the parameter to type_decorator
@type_converter(str) 
#Write a function return_int() that takes no arguments and returns the integer value 5
def return_int():
    return 5


#Pass int as the parameter to type_decorator
@type_converter(int) 
#Write a function return_string() that takes no arguments and returns the string value "not a number"
def return_string():
    return "not a number"

if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__) # This should print "str"
    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!") # This is what should happen
