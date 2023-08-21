
def check_palindrome(word):
    if word.lower()==word[::-1].lower():
        print('It is Palindrome')
    else:
        print('It is not a Palindrome')

word1=check_palindrome('Tacocat')
word2=check_palindrome('Madam')
word3=check_palindrome('Aadit')
word4=check_palindrome('Mom')