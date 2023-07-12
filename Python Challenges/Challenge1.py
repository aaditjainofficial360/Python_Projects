'''
Words
Difficulty: Medium
Question: The words in a paragraph were stored in a 2D list. Each list inside the given list corresponds to a sentence. The elements of this list are words of that sentence. You have to find the mean number of words in each sentence. The mean of n values x1, x2 …, xn = (∑xi)/n. Round off the result to 2 decimal places.
Examples:
Test Case 1:
Input - [[‘I’, ‘am’, ‘hungry’], [“Let’s”, ‘order’]]
Output - 2.5
Explanation - The first sentence has 3 words. The second one has 2. Mean = (3+2)/2 = 2.5
Test Case 2:
Input - [[‘We’, ‘know’, ‘what’, ‘we’, ‘are’], [‘But’, ‘know’, ‘not’, ‘what’, ‘we’, ‘may’, ‘be’]]
Output - 6.0
Explanation - First sentence has 5 words. Second has 7 words. Mean = 6.
'''
def mean_of_words(lst):
    total_length_of_words=0
    for i in lst:
        total_length_of_words+=len(i)
    total_length_of_a_sentence=len(lst)
    mean=total_length_of_words/total_length_of_a_sentence
    return mean
Input1=[['I','am','hungry'],["Let\’s",'order’']]
Input2=[['We','know','what','we','are'],['But','Know','not','what','we','may','be']]
Input3=[['I','am','the','king','of','this','industry'],['Bow','Down','to','me']]
Input4=[['My','Name','is','Aadit','Jain'],['I','Want','to','become','high','quality','data','scientist']]
print(mean_of_words(Input1))
print(mean_of_words(Input2))
print(mean_of_words(Input3))
print(mean_of_words(Input4))