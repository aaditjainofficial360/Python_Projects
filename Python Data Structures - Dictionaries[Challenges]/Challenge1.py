
tree_dict={}
with open('treeorderssubsetnodupes.csv','r') as excel_file:
    file=excel_file.readlines()[1:]
    for entry in file:
        tree_dict.update({entry[:3]:entry[4]})
print(tree_dict)
print('Length of Trees Dictionary :',len(tree_dict))