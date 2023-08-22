import pandas as pd

customer_data=pd.read_csv('mall_customers.csv')
customer_database=[]
headers=('Customer Id','Gender','Age','Annual Income','Spending Score')
customer_database.append(headers)
for entry in customer_data.values:
    customer_database.append(tuple(entry))

for row in customer_database:
    print(row)
