#Task 1: Hello
def hello():
    say_hi = "Hello!"
    return say_hi
print(hello())

#Task 2: Greet with a Formatted String
def greet(name):
    return (f"Hello, {name}!")
print(greet("Bob"))

#Task 3: Calculator
def calc(a, b, operation="multiply"):
    #If the value of a or b is not an integer or float, you cannot multiply them
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "You can't multiply those values!"
    match operation:
        case "add":
            try:
                return a+b
            except TypeError:
                return "You can't add those values!"
        case "subtract":
            try:
                return a-b
            except TypeError:
                return "You can't subtract those values!"
        case "divide":
            try:
                return a/b
            except ZeroDivisionError:
                return "You can't divide by 0!"
            except TypeError:
                return "You can't divide those values!"
        case "modulo":
            return a % b
        case "int_divide":
            try:
                return a//b
            except ZeroDivisionError:
                return "You can't divide by 0!"
            except TypeError:
                return "You can't divide those values!"
        case "power":
            try:
                return a**b
            except TypeError:
                return "You can't raise those values to the power of the other!"
        #default case of multiply
        case _: 
            try:
                return a*b
            except TypeError:
                return "You can't multiply those values!"
           
print(calc (1, 2, "add"))
print(calc (1, 2, "subtract"))
print(calc (1, 2, "divide"))
print(calc (1, 2, "modulo"))
print(calc (1, 2, "int_divide"))
print(calc(1,2, "power"))
print(calc(1,2))
print(calc("hi",2))

#Task 4: Data Type Conversion
def data_type_conversion(value, data_type):
    match data_type:
        case "float":
            try:
                return float(value)
            except ValueError:
                return (f"You can't convert {value} into a {data_type}.")
        case "str":
            try:
                return str(value)
            except ValueError:
                return (f"You can't convert {value} into a {data_type}.")
        case "int":
            try:
                return int(value)
            except ValueError:
                return (f"You can't convert {value} into a {data_type}.")

print(data_type_conversion(1, "float"))
print(data_type_conversion("potato", "float"))

#Task 5: Grading System, Using *args
def grade(*args):
    try:
        average = sum(args)/len(args)
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ValueError):
        return "Invalid data was provided."
print(grade(50,50))

#Task 6: Use a For Loop with a Range
def repeat(string, count):
    #Start off with an empty string
    new_string = ""

    #While count is greater than 0, add the string to the new string
    while count > 0:
        new_string += string
        #Remove one from the count every iteration
        count -= 1
    #When count = 0, return the new_string composed of the multiple iterations of string
    return new_string
 
print(repeat("banana",3))

#Task 7: Student Scores, Using **kwargs
def student_scores(positional, **kwargs):
    match positional:
        case "best":
            #If there is a max test score
            if max(kwargs.values()):
                #Return the keyword associated with the highest test score(value)
                return max(kwargs, key=kwargs.get)
        case "mean":
            #Add the values of the values (the different test score) and then divide them by how many tests score there are
            return sum(kwargs.values()) / len(kwargs)

#Task 8: Titleize, with String and List Operations
def titleize(title):
    new_title = []
    words = title.split()
    for i, word in enumerate(words):
        #If the word is the first or last in the list, capitalize it and add it to the new_title
        if i == 0 or i == len(words) -1 :
            new_title.append(word.capitalize())
        #If the word is "a", "on", "an", "the", "of", "and", "is", or "in", keep it lowercase and add it to the new_title
        elif word in ["a", "on", "an", "the", "of", "and", "is", "in"]:
            new_title.append(word.lower())
        #Any other word that is not the first, last, or "a", "on", "an", "the", "of", "and", "is", or "in", capitalize it and add it to the new_title
        else:
            new_title.append(word.capitalize())
        #Return a string and join the words in the list new_title together to make a capitalized title
    return " ".join(new_title)

print(titleize("The cat in the hat"))

#Task 9: Hangman, with more String Operations
def hangman(secret, guess):

    #Start off with an empty string to display the guess_result
    guess_result = ""

    #For every letter in the secret word check
    for letter in secret:
        #If the guess contains a letter in secret, concatenate the letter to the guess_result
        if letter in guess:
            guess_result += letter
        #Otherwise, concatenate an underscore to the guess_result
        else:
            guess_result += "_"
    
    return guess_result

print(hangman("alphabet", "a"))

#Task 10:  Pig Latin, Another String Manipulation Exercise
def pig_latin(string):
    #Start off with an empty string
    final = ""
    words = string.split()
    
    #For each word in the whole string
    for word in words:
        #If the string starts with a vowel (a,e,i,o,u), add/concatenate "ay" to the end of the word
        if word[0] in ["a", "e", "i", "o", "u"]:
            final += word + "ay"
        #If the string starts with "qu", add/concatenate "ay" to the end of the word after "qu"
        elif word[:2] == "qu":
            final += word[2:] + "qu" + "ay"
        #For square
        elif word[:3] == "squ":
            final += word[3:] + "squ" + "ay"
        else:
            #Go through each letter in each word
            for i, letter in enumerate(word):
                #When a letter is a vowel, stop there (position i), take the portion after that point [i:], add the portion before that point [:i], and then add "ay"
                if letter in ["a", "e", "i", "o", "u"]:
                    final += word[i:] + word[:i] + "ay"
                    break
        final += " "
    return final.strip()

print(pig_latin("apple"))
print(pig_latin("quack"))
print(pig_latin("print"))
