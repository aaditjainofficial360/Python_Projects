def Survival(lst,new_element,position):
    if len(lst)>5:
        return "List have more than 5 elements."
    elif len(lst)==5:
        lst[position]=new_element
        print(lst)
        return f'List updated with {new_element} element into the list !'
    else:
        lst.insert(position,new_element)
        print(lst)
        return f'List updated with {new_element} being added to the list !'
print(Survival([1,2,3,4,5],9,2))
    
