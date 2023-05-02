string=input("Enter your name: ").upper()
string_dict={}

for i in string:
    string_dict.update({i:string.count(i)})
print(string_dict)