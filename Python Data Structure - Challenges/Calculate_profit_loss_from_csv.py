import pandas as pd

sales_data=pd.read_csv('sales_data.csv')
profit_loss_list=[]
for row in sales_data.values:
    result=row[-2]-row[-1]
    if result>0:
        profit_loss_list.append((f"{row[0]} has made a profit of Rs.{result}"))
    else:
        profit_loss_list.append((f"{row[0]} has made a loss of Rs.{abs(result)}"))

for entry in profit_loss_list:
    print(entry)