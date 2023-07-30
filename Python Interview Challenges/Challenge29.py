'''
Given a String, perform its mirror imaging, return “Not Possible” if mirror image not possible using english characters.

Input : test_str = ‘boid’ Output : doib Explanation : d replaced by b and vice-versa as being mirror images.
Input : test_str = ‘gfg’ Output : Not Possible Explanation : Valid Mirror image not possible.
'''

def mirror_image(string):
    duplicate_image=string[::-1]
    if duplicate_image==string:
        return 'Not Possible'
    else:
        return duplicate_image

# Test-case 1
test_str1 = 'boid'
print(mirror_image(test_str1))

# Test-case 2
test_str2 = 'gfg'
print(mirror_image(test_str2))