#Task 2: Read a CSV File
import csv
import traceback

#Define a function
def read_employees():
    #Empty dictionary
    names = {}
    #Empty list
    rows = []

    try:
        with open('../csv/employees.csv', 'r') as file:
            #Read the CSV file
            reader = csv.reader(file)
            #Loop through the CSV file
            for index, row in enumerate(reader):
                #The first row in the dictionary (the column headers); store using 'fields'
                if index == 0:
                    names["fields"] = row
                #Otherwise, append it to the rows list
                else:
                    rows.append(row)

        #Stores all of the rows in the dictionary
        names["rows"] = rows
        #Return the dictionary
        return names

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

#Call the function as employees
employees = read_employees()

#Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)

#Calling the function for the employee id column
employee_id_column = column_index("employee_id")

#Task 4: Find the Employee First Name
#Make a function
def first_name(row_number):
    #Get the column index of the first name
    find_first_name = column_index("first_name")

    #Go to the row in the employee dictionary as 'row'
    row = employees["rows"][row_number]

    #Return the associated row with the first name
    return row[find_first_name]

print(first_name(2)) #Output: Lauren

#Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    #Function inside a function
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    #Call filter function
    matches=list(filter(employee_match, employees["rows"]))
    return matches

#Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

#Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    # Get the column index for the last names
    index_of_last_name = column_index("last_name")
 
    # Sort the list of rows with lambda
    employees["rows"].sort(key=lambda row: row[index_of_last_name])

    #Return the sorted list of rows
    return employees["rows"]

# Call the function and see the employee dictionary
sort_by_last_name()
print(employees)

#Task 8: Create a dict for an Employee
def employee_dict(row):
    #Create a dictionary by zipping column headers (fields) and its row value; skips the employee_id (index 0)
    return {key: value for key, value in zip(employees["fields"][1:], row[1:])}

#Prints the result of the function
print(employee_dict(employees["rows"][1]))
#Output: {'first_name': 'Thomas', 'last_name': 'Calderon', 'phone': '+64 +1-380-200-3211'} Dictionary for Thomas Calderon

#Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    #Blank dictionary to write in
    all_employees_dir = {}

    #Get the necessary values (key: rows in employee_id, value: employee_dict)
    #Iterate through them to create the new dictionary
    for row in employees["rows"]:
        #Employee_id is in row 0 (index 0)
        employee_id = row[0]
        #Use the employee_dict function to get employee_dict
        employee_info = employee_dict(row)
        #Store the data in the all_employees dictionary with the employee_id as the key
        all_employees_dir[employee_id] = employee_info

    return all_employees_dir

all_employees_dict()
print(all_employees_dict())

#Task 10: Use the os Module
import os

#Access the environment value and return its value
def get_this_value():
    what_is_this = os.environ.get('THISVALUE')
    return what_is_this

#Task 11: Creating Your Own Module
import custom_module

#Create a function to set the new secret and use the module you imported
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("banana")
print(custom_module.secret)

#Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    #Set blank dictionaries to be written in
    minutes1 = {}
    minutes2 = {}


    #Helper function - Helps with the conversion of dictionaries -> tuples
    def conversion_to_sets_and_tuples(rows, fields):
        return [tuple(row[field] for field in fields) for row in rows]


    #minutes1
    with open ('../csv/minutes1.csv', 'r') as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader]
        fields = reader.fieldnames

        #Converting the rows in the dictionary to tuples
        minutes1['fields'] = fields
        minutes1['rows'] = conversion_to_sets_and_tuples(rows, fields)

    #minute2
    with open ('../csv/minutes2.csv', 'r') as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader]
        fields = reader.fieldnames

        #Converting the rows in the dictionary to tuples
        minutes2['fields'] = fields
        minutes2['rows'] = conversion_to_sets_and_tuples(rows, fields)

    #Return both of the dictionaries (minutes1 and minutes2)
    return minutes1, minutes2

# Call the function and print out the dictionaries
read_minutes()
minutes1, minutes2 = read_minutes()

#Task 13: Create minutes_set
def create_minutes_set():
    #Convert minutes1 and minutes2 to sets
    set_minutes1 = set(minutes1["rows"])
    set_minutes2 = set(minutes2["rows"])

    #Combine both sets (mintutes1 and minutes2) into ONE set
    minute_union = set_minutes1.union(set_minutes2)

    #Return the combined set
    return minute_union

create_minutes_set()
minutes_set = create_minutes_set()

#Task 14:  Convert to datetime
from datetime import datetime

def create_minutes_list():
    #Convert to a list
    new_list = list(minutes_set)

    #Use the map() function to convert every entry on the list (name (unchanged), date (converted to datetime object)) into a tuple
    mapped_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), new_list))

    #Return the new mapped out list
    return mapped_list

#Call the create_minutes_list function and store the value in a global variable
minutes_list = create_minutes_list()
print(minutes_list)

#Task 15: Write Out Sorted List
def write_sorted_list():

    #Sort minute_list in ascending order (increasing) for datetime
    minutes_list.sort(key=lambda x: x[1])

    #Convert to a tuple; don't change the name
    new_minutes_list = tuple(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))

    #Open a CSV file
    with open('./minutes.csv', 'w') as file:

        #Use a csv.writer() to write out the resulting sorted data
        writer = csv.writer(file)

        #First row should be value of the fields from minute1 dict
        writer.writerow(minutes1["fields"])

        #Subsequent rows should be elements from the minutes_list
        writer.writerows(minutes_list) 

        return new_minutes_list
    
write_sorted_list()





