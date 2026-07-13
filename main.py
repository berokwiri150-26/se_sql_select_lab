# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd
# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')


# STEP 2
# Replace None with your code
df_first_five = pd.read_sql_query("SELECT employeeNumber, lastName FROM employees", conn)
print(df_first_five)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql_query("SELECT lastName, employeeNumber FROM employees", conn)
print(df_five_reverse)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql_query("SELECT lastName, employeeNumber AS ID FROM employees", conn)
print(df_alias)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql_query("""
SELECT *,
       CASE
           WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing') THEN 'Executive'
           ELSE 'Not Executive'
       END AS role
FROM employees
""", conn)
print(df_executive)

# STEP 6
# Replace None with your code
df_name_length = df_name_length = pd.read_sql_query("SELECT LENGTH(lastName) AS name_length FROM employees", conn)
print(df_name_length)

# STEP 7
# Replace None with your code
df_short_title = df_short_title = pd.read_sql_query("SELECT SUBSTR(jobTitle, 1, 2) AS short_title FROM employees", conn)
print(df_short_title)

# STEP 8
# Replace None with your code
sum_total_price = sum_total_price = pd.read_sql_query("""
SELECT ROUND(priceEach * quantityOrdered) AS total_price
FROM orderdetails
""", conn).sum()
sum_total_price.index = [0]

print(sum_total_price)

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql_query("""
SELECT orderDate,
       strftime('%d', orderDate) AS day,
       strftime('%m', orderDate) AS month,
       strftime('%Y', orderDate) AS year
FROM orders
""", conn)
print(df_day_month_year)

# Close the connection
conn.close()