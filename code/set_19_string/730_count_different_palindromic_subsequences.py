# Count Different Palindromic Sub-sequences
# Given a string S, find the number of different non-empty palindromic subsequences in S,
# and return that number modulo 10^9 + 7.
# A subsequence of a string S is obtained by deleting 0 or more characters from S.
# A sequence is palindromic if it is equal to the sequence reversed.
# Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.

# Example 1:
# Input:
# S = 'bccb'
# Output: 6
# Explanation:
# The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
# Note that 'bcb' is counted only once, even though it occurs twice.

# Example 2:
# Input:
# S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
# Output: 104860361
# Explanation:
# There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.

# Note:
# The length of S will be in the range [1, 1000].
# Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
# ========================================================================================
# Algorithm:
# TC: O(n^2). Two nested traversals are needed.
# SC: O(n^2). Matrix of size n*n is needed to store the dp array.
# ========================================================================================


# dp(i,j) is for s[i:j+1] palindrome number
# c is for single charactor for odd palindrome
# p is pair for even palindrome
def count_palindromic_subsequences_1(s):
    dp = {}

    def dfs(i, j):
        key = (i, j)
        if key in dp:
            return dp[key]
        c = ''
        p = []
        n = 1
        for l in range(i, j+1):
            if s[l] not in c:
                c += s[l]
                n += 1        # single character for odd palindrome
                r = j
            if s[l] not in p:
                while r > l:
                    if s[r] == s[l]:
                        p += [s[l]]
                        n += dfs(l+1, r-1)    # find the most wild closure for even palindrome
                        break
                    r -= 1
            if len(p) == 4 and len(c) == 4:
                break          # no more option
        dp[key] = n % (1e9 + 7)
        return dp[key]
    return int(dfs(0, len(s)-1) - 1)


# ====================================================================================
# Method-2 : explanation
# Assume that dp[i][j] is the number of different palindromic subsequences in range [i,j]
# if s[i] != s[j] so [i,j] is not a palindromic string, we can get rid of either s[i] or s[j]. We have:
# dp[i][j] = dp[i+1][j] + dp[i][j-1] - d[i+1][j-1]
# we must -d[i+1][j-1], because the range [i+1, j-1] is calculated twice.
#
# if s[i] == s[j] so
# dp[i][j] = dp[i+1][j-1] + s[i] {dp[i+1][j-1]} s[j] - duplicated elements between 2 sets
#
# Example: s = bbbabb // count = 8
# dp[1][4] = "bbab" = [b] + [bb] + [bbb] + [a] + [bab] = 5
# dp[0][5] = "bbbabb" = dp[1][4] + b{dp[1][4]}b - duplicated elements
# dp[0][5] = "bbbabb" = 5 + b[b]b + b[bb]b + b[bbb]b + b[a]b + b[bab]b - duplicated elements
# Here duplicated elements are :
#
# b[b]b = [bbb] = 1
# b[a]b = [bab] = 1
# dp[0][5] = 5 * 2 - 1 - 1 = 8
#
# The most important thing here is to calculate the number of duplicated elements.
# These elements will be in the range (i1,j1) (a sub range of [i,j]) where:
# i1 is the next position to the right from i so that s[i] = s[i1]
# j1 is the next position to the left from j so that s[j1] = s[j]
#
# all elements in [i1+1, j1-1] will be duplicated, because:
# s[i1] { [i1+1, j1-1] } s[j1] = s[i] { [i1+1, j1-1] } s[j]
# ===================================================================================


def count_palindromic_subsequences(s):
    n = len(s)
    table, prv, nxt, arr = [[0]*n for i in range(n)], [None]*n, [None]*n, [0]*n
    # print(nxt, prv, arr)
    for i in range(n):
        arr[i] = ord(s[i])-ord('a')
        print(arr)
    last = [None]*4
    for i in range(n):
        prv[i] = last[arr[i]]
        last[arr[i]] = i

    last = [None]*4
    for j in range(n-1,-1,-1):
        nxt[j] = last[arr[j]]
        last[arr[j]] = j

    for d in range(n):
        for i in range(n-d):
            j = i+d
            if i == j:
                table[i][j] = 1
            elif arr[i] != arr[j]:
                table[i][j] = table[i+1][j]+table[i][j-1]-table[i+1][j-1]
            else:
                i0, j0, extra = nxt[i], prv[j], 0
                if i0 is not None and j0 is not None:
                    extra = (-table[i0+1][j0-1]) if i0<j0 else (1 if i0==j0 else 2)
                table[i][j] = 2*table[i+1][j-1]+extra

            table[i][j] = (table[i][j]+10**9+7) if table[i][j]<0 else table[i][j]%(10**9+7)

    return table[0][n-1]


if __name__ == "__main__":

    input_str = 'bccb'    # output: 6
    # input_str = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'    # output: 104860361
    print(count_palindromic_subsequences(input_str))
