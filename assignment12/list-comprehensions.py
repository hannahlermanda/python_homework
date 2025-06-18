#Task 3: List Comprehensions Practice

import pandas as pd

#Read the contents of ../csv/employees.csv into a DataFrame
df = pd.read_csv("../csv/employees.csv")


#Create a list of the employee names, first_name + space + last_name
#If df is your dataframe, df.iterrows() gives an iterable list of rows.
#Each row is a tuple, where the first element of the tuple is the index
#The second element is a dict with the key/value pairs from the row
full_employee_names = [row['first_name'] + ' ' + row['last_name'] for _, row in df.iterrows()]

#All employee names before filtering (resulting list from the dataframe)
print(full_employee_names)

#Create another list from the previous list of names
names_with_e = [name for name in full_employee_names if 'e' in name]

#This list should include only those names that contain the letter "e". Print this list.
print("\nEmployee names that contain the Letter 'e':")
print(names_with_e)