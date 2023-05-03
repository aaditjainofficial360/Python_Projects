sentence='Hello My Name is Alpha Omega'
sentence="My name is Aadit Jain"
sentence_mapper=dict()
for i in range(len(sentence.split())):
    if i!=len(sentence.split())-1:
        sentence_mapper.update({sentence.split()[i]:sentence.split()[i+1]})
    else:
        sentence_mapper.update({sentence.split()[i]:-1})
print(sentence_mapper)
