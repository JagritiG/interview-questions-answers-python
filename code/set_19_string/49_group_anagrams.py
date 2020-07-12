# Group Anagrams
# Given an array of strings, group anagrams together.

# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# Note:
# All inputs will be in lowercase.
# The order of your output does not matter.
# ======================================================================================
# Algorithm:
# Hash table
# TC:
# SC:
# ========================================================================================


def group_anagrams(s):

    ht = dict()
    for word in s:
        sorted_word = "".join(sorted(word))
        if sorted_word not in ht:
            ht[sorted_word] = [word]
        else:
            ht[sorted_word].append(word)

    result = []
    for val in ht.values():
        result.append(val)

    return result


if __name__ == "__main__":

    input_str = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(input_str))
