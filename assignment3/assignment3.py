import pandas as pd

#Task 1: Introduction to Pandas - Creating and Manipulating DataFrames

#Task 1.1 - Create a DataFrame from a dictionary
#Creating a dictionary
people_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age':  [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

#Convert into a dataframe using pandas
df = pd.DataFrame(people_data)
print(df)

#Save the DataFrame in a variable called task1_data_frame
task1_data_frame = df

#Task 1.2 - Add a new column
task1_with_salary = task1_data_frame.copy()

#New Column as a DataFrame and add it to the copy
task1_with_salary['Salary'] = [70000, 80000, 90000]

print(task1_with_salary)

#Task 1.3 - Modify an Existing Column
task1_older = task1_with_salary.copy()

#Increment the ages by 1
task1_older['Age'] += 1

print(task1_older)

#Task 1.4 - Save the DataFrame as a CSV file
#Save the task1_older DataFrame to a file named employees.csv using to_csv(), do not include an index in the csv file
task1_older.to_csv('employees.csv', sep = ",", index= False)

employee_data = pd.read_csv('employees.csv')

#Check the contents of the file
with open('employees.csv', 'r') as file:
    print(file.read())


#Task 2: Loading Data from CSV and JSON
#Task 2.1 - Read data from a CSV file
#Load the CSV file from Task 1 into a new DataFrame saved to a variable task2_employees
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

#Task 2.2 - Read data from a JSON file
#Load this JSON file into a new DataFrame and assign it to the variable json_employees
json_employees = pd.read_json('additional_employees.json')

#Task 2.3 - Combine DataFrames
#Combine the data from the JSON file into the DataFrame Loaded from the CSV file and save it in the variable more_employees
more_employees = pd.concat([employee_data, json_employees], ignore_index=True)

print(more_employees)

#Task 3: Data Inspection - Using Head, Tail, and Info Methods
#Task 3.1 - Use the head() method
#Assign the first three rows of the more_employees DataFrame to the variable first_three
first_three = (more_employees.head(3))
print(first_three)

#Task 3.2 - Use the tail() method
#Assign the last two rows of the more_employees DataFrame to the variable last_two
last_two = more_employees.tail(2)
print(last_two)

#Task 3.3 - Get the shape of a DataFrame
#Assign the shape of the more_employees DataFrame to the variable employee_shape
employee_shape = more_employees.shape
print(employee_shape)

#Task 4 - Data Cleaning
#Task 4.1 - Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data
dirty_data = pd.read_csv('dirty_data.csv')

#Create a copy of the dirty data in the variable clean_data (use the copy() method)
clean_data = dirty_data.copy()

#Task 4.2 - Remove any duplicate rows from the DataFrame
clean_data = clean_data.drop_duplicates()
print(clean_data)

#Task 4.3 - Convert Age to numeric and handle missing values
#Convert to Numeric
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors = "coerce")
#Handle missing values (Keep it numeric)
clean_data["Age"] = clean_data["Age"].fillna(pd.NA)
print(clean_data)

#Task 4.4 - Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
#Replace known placeholders (unknown, n/a) with NaN
clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], pd.NA)
#Convert Salary to numeric
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors = "coerce")
print(clean_data)

#Task 4.5 - Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median
#Filling the missing numeric values of Age with the mean
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())

#Filling the missing numeric values of Salary with the median
clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())

print(clean_data)

#Task 4.6 - Convert Hire Date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors = "coerce")

print(clean_data)

#Task 4.7 - Strip extra whitespace and standardize Name and Department as uppercase
#Strip extra whitespace and standardize Name as uppercase
clean_data["Name"] = clean_data["Name"].str.strip()
clean_data["Name"] = clean_data["Name"].str.upper()

#Strip extra whitespace and standardize Department as uppercase
clean_data["Department"] = clean_data["Department"].str.strip()
clean_data["Department"] = clean_data["Department"].str.upper()

print(clean_data)
