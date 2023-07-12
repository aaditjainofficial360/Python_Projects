'''
Not today, Duplicate!
Difficulty: Hard
Question: Do you know about relational databases? They are the huge pools of data that store data in an efficient way for performing Create, Read, Update and Delete (CRUD) operations on data. To facilitate this, they employ many techniques - one of them being to store each set of unique data with a unique identifier, called primary key. There are other constraints that can be used as keys as well - for example in a customer database, customer email can be kept as a key besides the primary key, given that every customer email should be unique. In this case, it’s called a candidate key.
Here, you are the esteemed Database Administrator (DBA), and your task is to de-duplicate the data. Data de-duplication refers to the process of eliminating already existing duplicate data or preventing duplicate data from entering the database.
But real-world data is messy, containing lots of duplicates. Here, you are given incoming employee data that consists of their name, address, employee email, phone number, etc. Your job is to create a filter that removes incoming duplicates from the database you are given.
The incoming data is in the form of a list of tuples (DATA_KEY, NAME, EMAIL, ADDRESS, PHONE)
The following constraints are given:
DATA_KEY, EMPLOYEE_EMAIL and PHONE are the keys - that is, they should be unique.
Complete the function db_filter(data) so that it takes in incoming data as a list of tuples and returns a de-duplicated list containing only the data that satisfy the above constraints. In case of duplicates, keep the data that was stored first.
Input format: List of tuples
Output format: List of tuples
Examples:
Test Case 1:
Input: [(1, “A”, “a@b.com”, “23, Lake Avenue”, “919734536286”), (1, “B”, “a@b.com”, “23, Bard Colony”, “919734536286”)]
Output: [(1, “A”, “a@b.com”, “23, Lake Avenue”, “919734536286”)]
Explanation: The second entry violated the constraints that the fields DATA_KEY, EMPLOYEE_EMAIL and PHONE must be unique. So it was ignored.

'''
def db_filter(data):
    primary_key=list()
    result_set=list()
    for i in data:
        if i[0] in primary_key:
            pass
        else:
            primary_key.append(i[0])
            result_set.append(i)
    return result_set

Input1=[(1, 'A', 'a@b.com', '23', 'Lake Avenue', '919734536286'), (1, 'B', 'a@b.com', '23', 'Bard Colony', '919734536286')]

print(db_filter(Input1))