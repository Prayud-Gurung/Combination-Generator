import itertools

# elements = ['A', 'B', 'C']
# r = 2
# combinations = list(itertools.combinations(elements, r))
# print(combinations)


# elements = ['A', 'B', 'C']
# all_combinations = []
# for r in range(1, len(elements)+1):
#     all_combinations.extend(itertools.combinations(elements, r))
# print(all_combinations)


# word = "ab"
# combos = itertools.product(*[(c.lower(), c.upper()) for c in word])
# for combo in combos:
#     print("".join(combo))

# print(list(itertools.product([1, 2, 3], [9, 8, 7])))
# #output: [(1, 9), (1, 8), (1, 7), (2, 9), (2, 8), (2, 7), (3, 9), (3, 8), (3, 7)]


# output = list(itertools.permutations([1, 2, 3], r=2))
# print(output)

# output = list(itertools.combinations([1, 2, 3], r=2))
# print(output)

# output = list(itertools.combinations_with_replacement([1, 2, 3], r=2))
# print(output)

# word = "apple"
# combo_list = []
# for c in word:
#     output = (c.lower(), c.upper())
#     combo_list.append(output)
# combos = list(itertools.product(*combo_list))
# for combo in combos:
#     print("".join(combo))

# print(combo_list)


# word = "apple"
# combos = itertools.product(*[(c.lower(), c.upper()) for c in word])
# for combo in combos:
#     print("".join(combo))

# boxes = [(1,2), (3,4), (5,6)]

# print(list(itertools.product(boxes)))      # Without *, picks one tuple at a time
# # Output: [((1, 2),), ((3, 4),), ((5, 6),)]

# print(list(itertools.product(*boxes)))     # With *, picks one item from each tuple
# # Output: [(1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6)]

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = [['a', 'b', 'c'], 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
# c = [['a', 'b', 'c'], ['x', 'y', 'z']]
# print(list(itertools.product(*c)))

# xyz = ['x', 'y', 'z']
# num = [1, 2, 3]

# a = ['x', 1]
# b = ['y', 2]
c = [['x', 1, 'a'], ['y', 2, 'b'], ['9']]
print(list(itertools.product(*c)))