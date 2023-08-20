treeOrders10={}
trees_dict={}
with open('treeorderssubsetnodupes.csv','r') as excel_file:
    file=excel_file.readlines()[1:]
    for entry in file:
        if entry[:3] in trees_dict:
            trees_dict[entry[:3]]+=int(entry[-2])
        else:
            trees_dict.update({entry[:3]:int(entry[-2])})
for id in trees_dict:
    if trees_dict[id]>10:
        treeOrders10[id]=trees_dict[id]
print(treeOrders10)

#Using Dictionary Comprehension
treeOrders10={id:no_of_trees for id,no_of_trees in trees_dict.items() if no_of_trees>10}
print(treeOrders10)