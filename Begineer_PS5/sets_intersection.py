def intersection(A,B):
    return sorted(list(set(A)-set(B)))

print(intersection([1,2,3,4,5,6,7,8,9],[2,7,1,4]))