# Find All Anagrams in a String
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
# The order of output does not matter.

# Example 1:
# Input:
# s: "cbaebabacd" p: "abc"
# Output:
# [0, 6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:
# Input:
# s: "abab" p: "ab"
# Output:
# [0, 1, 2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# ======================================================================================
# Algorithm:
# Counter, Hash table, sliding window
# TC:
# SC:
# ========================================================================================
from collections import Counter


def find_anagrams(s, p):

    res = []
    s_len = len(s)
    p_len = len(p)

    if p_len > s_len:
        return res

    p_count = Counter(p)
    s_count = Counter()

    i = 0
    while i < s_len:
        s_count[s[i]] += 1
        if i >= p_len:
            if s_count[s[i-p_len]] == 1:
                del s_count[s[i-p_len]]
            else:
                s_count[s[i-p_len]] -= 1

        if p_count == s_count:
            res.append(i - p_len + 1)

        i += 1
    return res


if __name__ == "__main__":

    # s = "cbaebabacd"
    # p = "abc"   # output: [0, 6]
    # s = "abab"
    # p = "ab"   # [0, 1, 2]
    s = "ababababab"
    p = "aab"   # [0, 2, 4, 6]
    print(find_anagrams(s, p))
