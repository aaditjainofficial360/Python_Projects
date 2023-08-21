
with open('Meta_Platforms.txt','r') as file:
    meta_platforms=file.read()


words=[]
for word in meta_platforms.split():
    words.append(word)

count_of_words=len(words)

print(f'Total Words Count : {count_of_words}')