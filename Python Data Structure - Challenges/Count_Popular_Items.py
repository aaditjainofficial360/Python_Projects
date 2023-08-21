list_of_items_ordered=['Dahi Bhalla','Samosa','Dhokla','Jaleebi','Aloo Puri','Sambhar Idli','Samosa','Jaleebi','Aloo Chat','Dhokla','Jaleebi',
                       'Aloo Puri','Samosa','Jaleebi','Dhokla','Idli Sambhar','Aloo Chat','Samosa','AlOO Kachori','Dhokla','Samosa','Idli Sambhar',
                       'Aloo Chat','Aloo Puri','Chole Bhature','Dhokla']

items_dict={x:list_of_items_ordered.count(x) for x in list_of_items_ordered}
print(items_dict)
print('------------TOP SELLING ITEMS-------------')
sorted_quantity_list=sorted(list(items_dict.values()))
for item in items_dict:
    if items_dict[item] in sorted_quantity_list[-3:]:
        print(item)