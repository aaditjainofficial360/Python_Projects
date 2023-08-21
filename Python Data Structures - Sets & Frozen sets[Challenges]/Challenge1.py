matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

my_set={x for element in matrix for x in element}
print(my_set)