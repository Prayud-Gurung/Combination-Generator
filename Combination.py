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
    combos = list(itertools.product(*combo_options))
    for combo in combos:
        result.add("".join(combo))
    return result

def insert_symbol():#Over engineered
    word = "Apple"
    word_plus_sym = []
    for i in range(len(word)):
        for symbol in symbols:
            word_plus_sym.append(word[i:] + symbol + word[:i])
    print(word_plus_sym)

def replace():
    # print(combo_values)

    # a = word.replace(word[4], leet_dict[word[4]][0])

    # for i in range(len(word)):
    #     replaced_word = word
    #     for j in range(i+1):
    #         a = replaced_word[:j] + "x" + replaced_word[j+1:]
    #         # print(a)
    #         combination.add(a)
    # print(combination)

    # for i in range(len(word)):
    #     replaced_word = word
    # for j in range(i+1):
    #     if word[j] in leet_dict.keys():
    #         num_alt_chars = len(leet_dict[word[j]])
    #         if num_alt_chars > 1:
    #             for k in range(num_alt_chars):
    #                 a = replaced_word[:j] + leet_dict[word[j][k]] + replaced_word[j+1:]
    #         else:
    #             a = replaced_word[:j] + leet_dict[word[j]] + replaced_word[j+1:]
    #     # print(a)
    #     combination.add(a)

    # for i in range(len(word)):
    #     replaced_word = word
    # for j in range(i+1):
    #     if word[j] in leet_dict.keys():
    #         dictionary_values = leet_dict[word[j]]
    #         if len(dictionary_values) > 1:
    #             for index, k in enumerate(dictionary_values):
    #                 a = replaced_word[:j] + k + replaced_word[j+1:]
    #         # print(a)

    #         print("AA", leet_dict[word[j]])
            # else:
            #     a = replaced_word[:j] + leet_dict[word[j]] + replaced_word[j+1:]
        # combination.add(a)        

    # combo_values = []
    # for key in leet_dict.keys():
    #     for i in word:
    #         if(i == key):
    #             combo_values.append(leet_dict[key])
    # print(combo_values)

        # print(key)

    # itertools.product()
        

    # for i in range(len(word)):
    #     for j in range(i):
    #         if (word[j] in leet_dict.keys()):
    #             print(leet_dict[word[j]])
    #         else:
    #             print(word[j])
    pass

# apple = [0, 4]pple, a
    # combination = set()
    # for i in range(len(word)):
    #     for j in range(i):
    #         alt_char = leet_dict[word[i]]
    pass

def add_prefix(word):
    result = set()
    for words in common_prefixes:
        modified_word = words + word
        result.add(modified_word)
    return result

def add_suffix(word):
    result = set()
    for words in common_suffixes:
        modified_word = words + word
        result.add(modified_word)
    return result

def generate_password():
    word = "apple"
    combinations = set()
    combinations.update(try_upper_lower(word))
    combinations.update(add_prefix(word))
    combinations.update(add_suffix(word))
    print(combinations)
# insert_symbol()
generate_password()