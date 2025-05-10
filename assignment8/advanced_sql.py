import pandas as pd
import sqlalchemy as sa
import sqlite3
import os

#Database path as a variable
db_path = "./db/advanced_sql.db"

#Check if the database already exists
if os.path.exists(db_path):
    answer = input("The database exists. Do you want to recreate it (y/n)? ")
    if answer.lower() != 'y':
        exit(0)
    os.remove(db_path)

#Create the database
with sqlite3.connect(db_path, isolation_level='IMMEDIATE') as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    #Create the tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY,          
        customer_name TEXT,
        contact TEXT,
        street TEXT,
        city TEXT,
        postal_code TEXT,
        country TEXT,
        phone TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        phone TEXT      
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        price REAL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS line_items (
        line_item_id INTEGER PRIMARY KEY,
        order_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        FOREIGN KEY(order_id) REFERENCES orders(order_id),
        FOREIGN KEY(product_id) REFERENCES products(product_id)
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        employee_id INTEGER,
        date TEXT,
        FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY(employee_id) REFERENCES employees(employee_id)
    )
    """)

engine = sa.create_engine(f'sqlite:///{db_path}')

#List of tables to load from CSV files
tables = ["customers", "employees", "products", "orders", "line_items"]

#CSV folder path
csv_dir = os.path.expanduser("~/Downloads/python_class/python_homework/csv")

#Load data from CSVs into the tables
for table in tables:
    t_name = table.lower()
    csv_file = os.path.join(csv_dir, f"{table}.csv")
    if os.path.exists(csv_file):
        data = pd.read_csv(csv_file, sep=',')
        data.to_sql(t_name, engine, if_exists='append', index=False)
        print(f"Loaded data into {t_name} table.")
    else:
        print(f"CSV file for {table} not found: {csv_file}")

print("Database 'advanced_sql.db' populated successfully.")

#Task 1: Complex JOINs with Aggregation

#Connect
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# QL query 
    #Total price of each of the first 5 orders
    #JOIN the orders table with the line_items table and the products table
    #GROUP_BY the order_id
    #SELECT the order_id and the SUM of the product price times the line_item quantity
    #ORDER BY order_id and LIMIT 5
    #Print out the order_id and the total price for each of the rows returned
query = """
SELECT 
    o.order_id,
    SUM(p.price * li.quantity) AS total_price
FROM 
    orders o
JOIN 
    line_items li ON o.order_id = li.order_id
JOIN 
    products p ON li.product_id = p.product_id
GROUP BY 
    o.order_id
ORDER BY 
    o.order_id
LIMIT 5;
"""

#Do the query
cursor.execute(query)

#Fetch and print the results
results = cursor.fetchall()
for row in results:
    print(row)

#Output
#(1, 513.5)
#(2, 38.24)
#(3, 242.85000000000002)
#(4, 793.3299999999999)
#(5, 271.84)

#Task 2: Understanding Subqueries

query = """
SELECT 
    c.customer_name,
    AVG(order_totals.total_price) AS average_total_price
FROM 
    customers c
LEFT JOIN (
    SELECT 
        o.customer_id AS customer_id_b,
        SUM(p.price * li.quantity) AS total_price
    FROM 
        orders o
    JOIN 
        line_items li ON o.order_id = li.order_id
    JOIN 
        products p ON li.product_id = p.product_id
    GROUP BY 
        o.order_id
) AS order_totals
ON c.customer_id = order_totals.customer_id_b
GROUP BY 
    c.customer_id;
"""

#Execute and print results
cursor.execute(query)
results = cursor.fetchall()
print("\nAverage order price per customer:")
for row in results:
    print(row)

#Close the connection
conn.close()

#Output:
#Average Order Price Per Customer:
#('Short, Taylor and Brown', 430.1466666666667)
#('Glover-Hernandez', 493.46000000000004)
#('Conrad-Harris', 168.13)
#('Patterson-Smith', None)
#('Mccann-Thompson', 301.58500000000004)
#('Kelly-Oconnell', 301.71999999999997)
#('Stephens, King and Johnson', 26.02)
#('Williams-Mack', 165.44333333333333)
#('Clark-Brooks', 231.21000000000004)
#('Galloway-Coleman', 263.3633333333333)
#('Mills, Torres and Graham', 375.8)
#('Preston-Wright', 285.69)
#('Owens-Mclaughlin', 225.095)
#('Dean Ltd', 426.61666666666673)
#('Mills Inc', 278.41333333333336)
#('Perez and Sons', 248.1275)
#('Neal, Baxter and Thompson', 223.84333333333333)
#('Garcia-Mcgrath', 348.285)
#('Serrano, Armstrong and Taylor', 215.745)
#('Salas-Ruiz', 128.4)
#('Meyer Ltd', 331.06)
#('Williams-Higgins', 367.78)
#('Davis, Salinas and Johnson', 284.745)
#('Ross Ltd', 61.54)
#('Vasquez and Sons', 347.3066666666667)
#('Johnson Inc', None)
#('Smith-Moore', 360.33)
#('Bryant-Hinton', 377.32)
#('Reynolds, Pollard and Day', 41.96000000000001)
#('Weiss, Sanders and Clark', 141.29)
#('Lowe, Acevedo and Thompson', 172.18666666666664)
#('Chambers-Anderson', 221.298)
#('Delacruz-Powell', None)
#('Wise Group', 201.65333333333334)
#('Espinoza Inc', 141.64000000000001)
#('Burke, Wilkerson and Coleman', 445.265)
#('Cox-Moyer', 455.38)
#('Walsh, Costa and Oconnor', 239.9225)
#('Ray, Shaw and Miller', 456.45)
#('Proctor, Cooley and Coleman', 147.9)
#('Hogan Inc', 293.65333333333336)
#etc.

#Task 3: An Insert Transaction Based on Data

#Get the Customer ID from customers for Perez and Sons
#Output (16,)

#Find the Employee ID for Miranda Harris
#Output: (7,)

#Top 5 least expensive product IDs
#(18,)
#(43,)
#(9,)
#(44,)
#(31,)


#Get a new order ID using the customer ID and Employee ID and the date
#Output: (250,)

with sqlite3.connect(db_path) as conn:
    #Ensure foreign keys
    conn.execute("PRAGMA foreign_keys = 1")

    #Begin transaction
    conn.execute("BEGIN")

    cursor = conn.cursor()

    #Customer ID for Perez and Sons
    cursor.execute("""
        SELECT customer_id 
        FROM customers 
        WHERE customer_name = 'Perez and Sons';
    """)
    customer_id = cursor.fetchone()[0]

    #Employee ID for Miranda Harris
    cursor.execute("""
        SELECT employee_id 
        FROM employees 
        WHERE first_name = 'Miranda' 
          AND last_name = 'Harris';
    """)
    employee_id = cursor.fetchone()[0]

    #Select the Product IDs from Products in Ascending (least to greatest); 5 max
    cursor.execute("""
        SELECT product_id 
        FROM products 
        ORDER BY price ASC 
        LIMIT 5;
    """)
    product_ids = [row[0] for row in cursor.fetchall()]

    #Create the order and get its order_id
    cursor.execute("""
        INSERT INTO orders (customer_id, employee_id, date)
        VALUES (?, ?, DATE('now'))
        RETURNING order_id;
    """, (customer_id, employee_id))
    order_id = cursor.fetchone()[0]

    #Insert the 5 lowest items with a quantity of 10 each
    cursor.executemany("""
        INSERT INTO line_items (order_id, product_id, quantity)
        VALUES (?, ?, 10);
    """, [(order_id, prod_id) for prod_id in product_ids])

    #Commit the transaction
    conn.commit()

    #Print new product order
    cursor.execute("""
        SELECT 
          li.line_item_id, 
          li.quantity, 
          p.product_name
        FROM line_items li
        JOIN products p 
          ON li.product_id = p.product_id
        WHERE li.order_id = ?;
    """, (order_id,))

    print("\nOrder_id =", order_id)
    for line_item_id, qty, prod_name in cursor.fetchall():
        print(line_item_id, qty, prod_name)


#Task 4: Aggregation with HAVING
#Output: (1, 'Cindy', 'Wade', 12)
#(2, 'David', 'Thornton', 13)
#(3, 'Lauren', 'Martinez', 14)
#(4, 'Kenneth', 'White', 8)
#(5, 'James', 'Torres', 13)
#(6, 'Tracy', 'Foster', 14)
#(7, 'Miranda', 'Harris', 12)
#(8, 'Destiny', 'Nguyen', 11)
#(9, 'Phillip', 'Williams', 13)
#(10, 'Kelli', 'Bowman', 14)
#(11, 'Gregory', 'Pittman', 16)
#(12, 'Natasha', 'Hoover', 9)
#(13, 'Gregory', 'Jackson', 12)
#(14, 'David', 'Clark', 11)
#(15, 'Sarah', 'Shepherd', 9)
#(17, 'Logan', 'Lopez', 16)
#(18, 'Donald', 'Hunt', 12)
#(19, 'Matthew', 'Meyers', 18)
#(20, 'Thomas', 'Calderon', 11)



#Find all employees associated with more than 5 orders.  
#You want the first_name, the last_name, and the count of orders.
#You need to do a JOIN on the employees and orders tables, and then use GROUP BY, COUNT, and HAVING.


#Connect
with sqlite3.connect(db_path) as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cur = conn.cursor()

    print("\nEmployees with more than 5 orders:")

    #Select the employee_id, first name, last name, and the number of orders each emplyee has; join them on employee and orders table
    query = """
    SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
    FROM employees e
    JOIN orders o ON e.employee_id = o.employee_id
    GROUP BY e.employee_id
    HAVING COUNT(o.order_id) > 5;
    """

    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

#Close the connection
conn.close()