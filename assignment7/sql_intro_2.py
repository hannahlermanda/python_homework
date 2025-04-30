#Task 5: Read Data into a DataFrame

import sqlite3
import pandas as pd

#Connect to the database
with sqlite3.connect("../db/lesson.db") as conn:
    #Write the SQL query with a JOIN statement
    sql_query = """
    SELECT li.line_item_id, li.quantity, li.product_id, p.product_name, p.price
    FROM line_items li
    JOIN products p ON li.product_id = p.product_id;
    """
    
    #Read the query results into a pandas DataFrame
    df = pd.read_sql_query(sql_query, conn)
    
    #Print the first five lines
    print(df.head())

    #Add a column to the DataFrame called "total". This is the quantity times the price
    df['total'] = df['quantity'] * df['price']

    #Print the first five lines
    print(df.head())

    #Add groupby() code to group by the product_id.
    #Use an agg() method that specifies 'count' for the line_item_id column, 'sum' for the total column, and 'first' for the 'product_name'.
    grouped_by_product_id = df.groupby('product_id').agg(
        line_item_count=('line_item_id', 'count'),
        total_sum=('total', 'sum'),
        first_product_name=('product_name', 'first')
    )

    #Print the first 5 lines
    print(grouped_by_product_id.head())

    #Sort the DataFrame by the product_name column
    grouped_by_product_id = df.sort_values(by='product_name', ascending=True)

    #Print the first 5 lines
    print(grouped_by_product_id.head())

    #Add code to write this DataFrame to a file order_summary.csv, which should be written in the assignment7 directory.
    grouped_by_product_id.to_csv('order_summary.csv', index=False)

    #Verify that this file is correct.
    check_order_summary = pd.read_csv('order_summary.csv')
    print(check_order_summary.head())