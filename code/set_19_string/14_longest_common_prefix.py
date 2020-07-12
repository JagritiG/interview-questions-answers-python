# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Note:
# All given inputs are in lowercase letters a-z.
# ======================================================================================
# Algorithm:
# Iterate across all the words and check if all the letters at a certain index is the same.
# 1. Find minimum length word in the given input string, because length of lcp would not be
# greater than the minimum length word.
# 2. Check for each character of all the words are same or not
# 3. If characters match, return lcp, otherwise return ""
# TC: O(n*minlen)
# SC:
# ========================================================================================


def longest_common_prefix(s):

    if len(s) == 0:
        return ""

    min_len = len(s[0])

    for i in s:
        min_len = min(min_len, len(i))

    lcp = ""
    i = 0
    while i < min_len:

        char = s[0][i]
        for j in range(1, len(s)):
            if s[j][i] != char:
                return lcp
        lcp = lcp + char
        i += 1

    return lcp


if __name__ == "__main__":

    # input_str = ["flower", "flow", "flight"]
    input_str = ["dog", "racecar", "car"]
    print(longest_common_prefix(input_str))
