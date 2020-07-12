# Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

# Example 1:
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# ========================================================================================
# Algorithm:
# Hash table, two pointer, sliding window
# TC: O(n)
# SC: O(n)
# ========================================================================================


def length_of_longest_substring(s):

    if len(s) == 0:
        return 0

    ht = dict()
    max_length = start = 0

    for i in range(len(s)):

        if s[i] in ht and start <= ht[s[i]]:
            start = ht[s[i]] + 1
        else:
            max_length = max(max_length, i-start+1)
        ht[s[i]] = i

    return max_length


if __name__ == "__main__":

    # input_str = "abcabcbb"    # output: 3
    # input_str = "bbbbb"    # output: 1
    input_str = "pwwkew"    # output: 3
    print(length_of_longest_substring(input_str))
