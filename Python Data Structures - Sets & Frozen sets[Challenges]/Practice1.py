'''Lego Blocks'''
group1 = {'Light Yellow','Brick Red','Brick Yellow','Light Green','Orange'}
group2 = {'Pink','Rose','Light Brown','Bright Red','Bright Blue'}
group3 = {'Light Blue','Light Red','Medium Red','Medium Blue','Light Grey'}

# Contains all the lego blocks of all colors
all_blocks=group1.union(group2,group3)
print("All Blocks :",all_blocks)
print('Length:',len(all_blocks))
print('-'*20)

# Contains sharing lego blocks
common_blocks=group1.intersection(group2,group3)
print("Common Blocks :",common_blocks)
print('Length:',len(common_blocks))
print('-'*20)

# Contains unique lego blocks of group 1
unique_blocks_of_gp1=group1.difference(group2,group3)
print(unique_blocks_of_gp1)
print('Length:',len(unique_blocks_of_gp1))
print('-'*20)

# Contains unique lego blocks of group 1 and group 2
unique_blocks_of_gp1_and_gp2=group1.symmetric_difference(group2)
print("All unique lego blocks in group 1 & group 2 :",unique_blocks_of_gp1_and_gp2)
print("Length:",len(unique_blocks_of_gp1_and_gp2))
print('-'*20)

# Contains subsets/supersets of lego blocks
subset1=group1.issubset(group3)
if subset1:
    print("Group 1 is a subset of Group 3")
else:
    print("Group 1 is not a subset of Group 3")

superset1=group1.issuperset(group2)
if superset1:
    print('Group 1 is a superset of Group 2')
else:
    print("Group 1 is not a superset of Group 2")