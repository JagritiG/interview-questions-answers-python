# Implement strStr()
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string.
# This is consistent to C's strstr() and Java's indexOf().
# ======================================================================================
# Algorithm:
# TC: O(n)
# SC:
# ========================================================================================


def str_str(haystack, needle):

    if len(needle) == 0:
        return 0

    i = 0
    while i <= len(haystack) - len(needle):
        if haystack[i:i+len(needle)] == needle:
            return i
        i += 1

    return -1


if __name__ == "__main__":

    # haystack = "hello"
    # needle = "ll"
    haystack = "aaaaa"
    needle = "bba"
    # haystack = "mississippi"
    # needle = "pi"

    print(str_str(haystack, needle))
