'''
Write a python program to remove empty tuples from the given list:
Examples:

Input : tuples = [(), (‘ram’,’15’,’8′), (), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”,”),()]
Output : [(‘ram’, ’15’, ‘8’), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”, ”)]

Input : tuples = [(”,”,’8′), (), (‘0′, ’00’, ‘000’), (‘birbal’, ”, ’45’), (”), (),  (”,”),()]
Output : [(”, ”, ‘8’), (‘0′, ’00’, ‘000’), (‘birbal’, ”, ’45’), (”, ”)]
'''

def remove_tuples(lst):
    new_lst=[x for x in lst if x!=()]
    return new_lst

print(remove_tuples([(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (", "),()]))

print(remove_tuples([(",",'8'), (), ('0','00','000'), ('birbal', '' , '45'), (""), (),  (","),()]))