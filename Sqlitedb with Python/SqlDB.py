import sqlite3

# Connect to DB
conn=sqlite3.connect('Aadit-Test DB.db')

# Create a Cursor
cursor=conn.cursor()

# Create a table
# cursor.execute('''
# CREATE TABLE Customers (
# ID INTEGER,
# NAME TEXT,
# EMAIL TEXT);
# ''')

# Drop a Table
# cursor.execute('DROP TABLE Customers')

# Inserting the rows in the created table one by one

# cursor.execute('''
# INSERT INTO Customers VALUES(1,'Aadit Jain','jaina17@corning.com')
# ''')
# cursor.execute('''
# INSERT INTO Customers VALUES(2,'Jayanta Basak','basakj@corning.com')
# ''')
# cursor.execute('''
# INSERT INTO Customers VALUES(3,'Swati Savalkar','savalkars@corning.com')
# ''')
# cursor.execute('''
# INSERT INTO Customers VALUES(4,'Pranali Tawale','tawalep@corning.com')
# ''')

# Inserting the records in a single query
info=[(1,'Aadit Jain','jaina17@corning.com'),(2,'Jayanta Basak','basakj@corning.com'),
      (3,'Swati Savalkar','savalkars@corning.com'),(4 ,'Pranali Tawale','tawalep@corning.com')]

# Population of Data using for loop using Insert query
# for i in info:
#     conn.execute(f'''
#     INSERT INTO Customers VALUES {i}
#     ''')

look_up_table='''
SELECT * FROM Customers
'''
# No need to give Ids . It has rowid as its default column. rowid is a primary key
look_up_table_automatic_rowid='''
SELECT rowid,* FROM Customers
'''
cursor.execute(look_up_table)
# print(cursor.fetchall()) # It presents the records as a tuples in a list.
# print(cursor.fetchone()) # Output- None
# print(cursor.fetchmany(4)) # Output- []

# To fetch all records one by one using For Loop in a list of tuples
all_records=cursor.fetchall()
# for i in all_records:
#     print(i)

# Printing Only IDs and Names
# for i in all_records:
#     print(i[0],i[1])

# Printing Only Names
# for i in all_records:
#     print(i[1])

# Where Clause
# Case When Swati is absent/On-Leave
# cursor.execute('SELECT * FROM Customers WHERE ID<>3')
# print('The Present attendees are as follows: ')
# for i in cursor.fetchall():
#     print(i[1])
# print()
print()
cursor.execute('SELECT NAME FROM Customers WHERE NAME LIKE \'%Jain\'')
for j in cursor.fetchall():
    print(j[0])
print()
print('Command Executed Successfully !')
# Commit our command
conn.commit()

# Close the Connection
conn.close()
