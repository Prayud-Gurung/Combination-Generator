import itertools

common_prefixes = ['my', 'the', 'super', 'ultra', '0x', 'root', 'king', 'admin']
common_suffixes = ['123', '007', '2023', '2024', '2025', '321', '69', '420', '!', '@', '#', '666', '777']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

leet_dict = {
    'a': ['@', '4'],
    'b': ['8'],
    'e': ['3'],
    'g': ['9'],
    'i': ['1', '!'],
    'l': ['1', '|'],
    'o': ['0'],
    's': ['$', '5'],
    't': ['7'],
    'z': ['2']
}

def try_upper_lower(word):
    combo_options = []
    result = set()
    for char in word:
        combo_options.append((char.upper(), char.lower()))
    # print(combo_options) #[('A', 'a'), ('P', 'p'), ('P', 'p'), ('L', 'l'), ('E', 'e')]
    combos = list(itertools.product(*combo_options))
    # print(combos)#[('A', 'P', 'P', 'L', 'E'), ('A', 'P', 'P', 'L', 'e'), ('A', 'P', 'P', 'l', 'E')]
    for combo in combos:
        result.add("".join(combo))
    return result

def replace(word):
    combo_options = []#[['a', '@', '4'], ['p'], ['p'], ['l', '1', '|'], ['e', '3']]
    combinations = set() 
    for char in word:
        if char.lower() in leet_dict:
            combo_options.append([char] + leet_dict[char.lower()])
            # print("Combinations:", [char] + leet_dict[char.lower()])#['a', '@', '4']
        else:
            combo_options.append([char])
    # print("char options: ", chars_options) #[['a', '@', '4'], ['p'], ['p'], ['l', '1', '|'], ['e', '3']]
    product_list = list(itertools.product(*combo_options))
    # print("Product list: ",product_list) #[('a', 'p', 'p', 'l', 'e'), ('a', 'p', 'p', 'l', '3'), ('a', 'p', 'p', '1', 'e')]

    for item in product_list:
        combinations.add("".join(item))
    return combinations

def add_symbol(word):
    result = []
    for i in range(len(word)):
        for symbol in symbols:
            result.append(word[i:] + symbol + word[i:])
    return result

def add_prefix(combinations):
    result = set()
    for combination in combinations:
        for words in common_prefixes:
            modified_word = words + combination
            result.add(modified_word)
            result.add(2 * words + combination)
    return result

def add_suffix(combinations):
    result = set()
    for combination in combinations:
        for words in common_suffixes:
            modified_word = combination + words
            result.add(modified_word)
            result.add(combination + words * 2)
    return result

def add_(combinations):
    result = set()
    for combination in combinations:
        for year in ['1999', '2000', '2012', '2020', '2024', '2025']:
            result.add(year + combination)
            result.add(combination + year)
    return result

word = input("Enter word:")
combinations = set()
combinations.update(try_upper_lower(word))
combinations.update(add_symbol(word))
combinations.update(replace(word))
combinations.update(add_prefix(combinations))
combinations.update(add_suffix(combinations))
combinations.update(add_(combinations))
combinations.add(word)
print("total combination: ", len(combinations))

with open("/Users/prayudgurung/Desktop/Cybersecurity/CombinationGenerator/passlist.txt", "w") as file:
    for passwords in list(combinations):
        file.write(passwords+"\n")