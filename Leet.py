leet_dict = {'a': ['@','4'],
             'p': ['2']}
word = "apple"
variants = set([word])

for i, c in enumerate(word):
    if c in leet_dict:
        for rep in leet_dict[c]:
            variants.add(word[:i] + rep + word[i+1:])
            
print(variants)