#Task 1: Writing and Testing a Decorator

import logging

#This should log the name of the called function (func.__name__), the input parameters of that were passed
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
# The value the function returns, to a file ./decorator.log.
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

#Declare a decorator called logger_decorator.
def logger_decorator(func):
    #function: <the function name> positional parameters:
    def logger_func(*args, **kwargs):
        #function: <the function name> positional parameters:
        result = func(*args, **kwargs)

        #<a list of the positional parameters, or "none" if none are passed>
        positional = list(args) if args else "none"

         #keyword parameters: <a dict of the keyword parameters, or "none" if none are passed>"
        keyword = kwargs if kwargs else "none"

        # Create the log message string
        log_msg = (
            f"function: {func.__name__}\n"
            f"positional parameters: {positional}\n"
            f"keyword parameters: {keyword}\n"
            f"return: {result}\n"
            "------------------------------"
        )

        # Log the message at INFO level
        logger.log(logging.INFO, log_msg)

        # Return the result from the original function
        return result
    
    # return: <the return value>
    return logger_func

#Declare a function that takes no parameters and returns nothing. 
@logger_decorator
def hiya():
    print("Hello, World!")

#Declare a function that takes a variable number of positional arguments and returns True
@logger_decorator
def check_args(*args):
    return True

#Declare a function that takes no positional arguments and a variable number of keyword arguments, and that returns logger_decorator
@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator

#Call each of these three functions, passing parameters for the functions that take positional or keyword arguments.
if __name__ == "__main__":
    hiya()

    check_args(1, 2, 3, "a", "b")

    return_decorator(name="Crush", age=150)
