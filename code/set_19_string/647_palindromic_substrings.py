# Palindromic Substrings
# Given a string, your task is to count how many palindromic substrings in this string.
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

# Note:
# The input string length won't exceed 1000.
# ========================================================================================
# Algorithm:
# Use a dynamic programming table. Have three loops, the last loop is nested.
# The first loop will look at single characters, the second will look at double characters,
# and the third nested loop will look at characters length 3 to n. Keep true/false in a boolean table.
# Update count for each non-zero elements of dp and return the count <-- result
# TC: O(n^2). Two nested traversals are needed.
# SC: O(n^2). Matrix of size n*n is needed to store the dp array.
# ========================================================================================


def count_substrings(s):

    n = len(s)

    # dp[i][j] is 1 if substring s[i..j] is palindrome,
    # else 0
    dp = [[0 for j in range(n)] for i in range(n)]

    count = 0
    # All substrings of length 1 are palindromes
    i = 0
    while i < n:
        dp[i][i] = 1
        i += 1
        count += 1

    # Find palindromic substring of length 2
    i = 0
    while i < n - 1:
        if s[i] == s[i+1]:
            dp[i][i+1] = 1
            count += 1
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
                count += 1

            i += 1
        substr_len += 1

    return count


if __name__ == "__main__":

    # input_str = "abc"    # output: 3
    input_str = "aaa"    # output: 6
    print(count_substrings(input_str))
