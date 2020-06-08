# mydict = {1: 'a', 2: 'b'}
# for i, (k, v) in enumerate(mydict.items()):
#     print("index: {}, key: {}, value: {}".format(i, k, v))

# my_list = ['apple', 'banana', 'grapes', 'pear']
# for c, value in enumerate(my_list, 1):
#     print(c, value)


# my_list = ['apple', 'banana', 'grapes', 'pear']
# counter_list = list(enumerate(my_list, 1))
# print(counter_list)


# values = (2, -1, 1)
# # Test if all items in values tuple are zero
# if all(v == 0 for v in values):
#     print(set(values))

# a = [-1, 0, 1]
# b = [0, 1, -1]
# print(set(a) & set(b))

# s1 = [-1, 0, 1]
# list2 = [0, 1, -1]
# for x in range(len(list2), -1, -1):
#     print(x)

#
# print(set(list1).difference(set(list2))) # returns {1, 2}

# list2 = [0, 0, 0]
# l = set(list2)
# print(l)


# lst = [1, 3, 5, 5, 3, 7, 5, 2, 5]
# sorted(lst)
#
# for e in sorted(lst):
#     print(e)

# a = 5 % 4
# print(a)


# Program to transpose a matrix using a nested loop

# X = [[12, 7],
#      [4, 5],
#      [3, 8]]
#
# # result = [[0, 0, 0],
# #           [0, 0, 0]]
# result = [[0]]
#
# # iterate through rows
# for i in range(len(X)):
#     # iterate through columns
#     for j in range(len(X[0])):
#         result[j][i] = X[i][j]
#
# for r in result:
#     print(r)


# a = 5//2 + 1
# print(a)

# Creates a list containing 5 lists, each of 8 items, all set to 0
# n = 3
# matrix = [[0 for x in range(n)] for y in range(n)]
# print(matrix)

# create matrix
import numpy as np

# m = 3
# n = 2

# matrix = np.zeros((m, n), dtype=int)
# matrix = [[0 for x in range(n)] for y in range(m)]
# matrix = [[0] * n] * m
# print(matrix)
# ====================================

# Max of a matrix
matrix = [[1, 2, 4], [8, 9, 0]]
print(max(map(max, matrix)))

