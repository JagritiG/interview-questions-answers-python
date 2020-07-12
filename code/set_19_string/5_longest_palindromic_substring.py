# Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.

# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: "cbbd"
# Output: "bb"
# ========================================================================================
# Algorithm:
# Use a dynamic programming table. Have three loops, the last loop is nested.
# The first loop will look at single characters, the second will look at double characters,
# and the third nested loop will look at characters length 3 to n. Keep true/false in a boolean table.
# TC: O(n^2). Two nested traversals are needed.
# SC: O(n^2). Matrix of size n*n is needed to store the dp array.
# ========================================================================================


# This function prints longest palindromic substring
# and returns length of the longest palindromic substring
def longest_palindrome(s):

    n = len(s)

    # dp[i][j] is 1 if substring s[i..j] is palindrome,
    # else 0
    dp = [[0 for j in range(n)] for i in range(n)]

    # All substrings of length 1 are palindromes
    max_length = 1
    i = 0
    while i < n:
        dp[i][i] = 1
        start = i
        i += 1

    # Find palindromic substring of length 2
    start = 0
    i = 0
    while i < n - 1:
        if s[i] == s[i+1]:
            dp[i][i+1] = 1
            start = i
            max_length = 2
        i += 1

    # Find palindromic substring of length >= 3
    # l is length of substring
    substr_len = 3
    while substr_len <= n:
        # Starting index i
        i = 0
        while i < n - substr_len + 1:

            # calculate the ending index of substring
            j = i + substr_len - 1

            # Check if substring, from ith index
            # to jth index, a palindrome or not
            if s[i] == s[j] and dp[i+1][j-1] == 1:
                dp[i][j] = 1

                if substr_len > max_length:
                    start = i
                    max_length = substr_len

            i += 1
        substr_len += 1

    return s[start:start+max_length]


if __name__ == "__main__":

    input_str = "babad"    # output: bab or aba
    # input_str = "cbbd"    # output: bb
    # input_str = "aaaabbaa"  # output: aabbaa
    # input_str = "ab"  # output: a
    # input_str = " "  # output:
    # input_str = "abcde"  # output: a
    print(longest_palindrome(input_str))
