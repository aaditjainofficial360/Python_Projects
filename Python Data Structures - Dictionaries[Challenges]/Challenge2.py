trees_dict={}
with open('TreeOrdersSubset.csv','r') as excel_file:
    file=excel_file.readlines()
    for entry in file:
        if entry[:3] in trees_dict:
            trees_dict[entry[:3]]+=int(entry[-2])
        else:
            trees_dict.update({entry[:3]:int(entry[-2])})
print(trees_dict)