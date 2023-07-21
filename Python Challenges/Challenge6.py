''''
Create acronyms
Difficulty: Medium
Question: Given a string with words separated by spaces, create an acronym by taking the first letter of each word. The output string should be in upper case.
Examples:
Test Case 1:
Input - ‘Laboratory for Physicists’
Output - ‘LFP’
Explanation - First letter of ‘laboratory’ is L. First letter of ‘for’ is F. For ‘Physicists’ it’s P. So our acronym becomes LFP.
Test Case 2:
Input - ‘State Bank of India’
Output - ‘SBOI’
Explanation - First letter of ‘state’ is S. For Bank it’s B, for ‘of’ it’s O, for India it’s I. So our acronym becomes SBOI.
'''

def create_acronyms(string):
    output=''
    for i in string.split():
        output+=i[0].upper()
    return output

Input1 ='Laboratory for Physicists'
print(create_acronyms(Input1))

Input2 ='State Bank of India'
print(create_acronyms(Input2))
