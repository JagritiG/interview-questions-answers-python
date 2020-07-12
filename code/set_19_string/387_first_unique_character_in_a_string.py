# First Unique Character in a String
# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1.

# Examples:
# s = "leetcode"
# return 0.

# s = "loveleetcode"
# return 2.
# ======================================================================================
# Algorithm:
# Hash table
# TC: O(n)
# SC: O(1)
# ========================================================================================


def first_unique_char(s):

    if len(s) == 0:
        return -1

    ht = dict()

    for i, e in enumerate(s):
        if e not in ht:
            ht[e] = [i]
        else:
            ht[e].append(i)

    for k, v in ht.items():
        if len(v) == 1:
            return s.index(k)

    return -1


if __name__ == "__main__":

    # input_str = "leetcode"   # output: 0
    # input_str = "loveleetcode"   # output: 2
    input_str = ""
    print(first_unique_char(input_str))
