# Given a string find longest palindromic subsequence in this string.

# Example 1:
# Input:
# S = 'abcdca'
# Output: 5
# Explanation: acdca
# ========================================================================================
# Algorithm:
# Similar to substring except use the table to keep track of longest length instead of boolean flag.
# If the characters on the end are the same, add the longest palindrome plus 2.
# Or get the max from [i][j-1] or [i+1][j]
# TC: O(n^2). Two nested traversals are needed.
# SC: O(n^2). Matrix of size n*n is needed to store the dp array.
# ========================================================================================


# Method-1: Dynamic programming
# This function prints longest palindromic subsequence
# and returns length of the longest palindromic subsequence
def longest_palindromic_subsequence(s):

    n = len(s)
    idx = []
    seq = ""

    dp = [[0 for j in range(n)] for i in range(n)]

    # All subsequence of length 1 are palindromes
    i = 0
    while i < n:
        dp[i][i] = 1
        i += 1

    # Find palindromic subsequence of length 2
    start = 0
    i = 0
    while i < n - 1:
        if s[i] == s[i+1]:
            dp[i][i+1] = 2
        else:
            dp[i][i+1] = 1
        i += 1

    # Find palindromic subsequence of length >= 3
    # l is length of substring
    subseq_len = 3
    while subseq_len <= n:
        # Starting index i
        i = 0
        while i < n - subseq_len + 1:

            # calculate the ending index of subsequence
            j = i + subseq_len - 1

            # Check for subsequence from ith index
            # to jth index
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

            i += 1
        subseq_len += 1

    return dp[0][n-1]


# Method-2: Recursive
def calculate_recursive(s, start, subseq_len):

    if subseq_len == 1:
        return 1

    if subseq_len == 0:
        return 0

    if s[start] == s[start+subseq_len-1]:
        return 2 + calculate_recursive(s, start+1, subseq_len-2)
    else:
        return max(calculate_recursive(s, start+1, subseq_len-1), calculate_recursive(s, start, subseq_len-1))


if __name__ == "__main__":

    input_str = 'abcdca'    # output: 5, acdca
    # print(calculate_recursive(input_str, 0, len(input_str)))
    print(longest_palindromic_subsequence(input_str))

