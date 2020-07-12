# Reverse Words in a String
# Given an input string, reverse the string word by word.

# Example 1:
# Input: "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

# Note:
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces.
# However, your reversed string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the reversed string.

# Follow up:
# For C programmers, try to solve it in-place in O(1) extra space.
# ======================================================================================
# Algorithm:
# TC:
# SC:
# ========================================================================================


def reverse_words(s):

    st = s.split()
    rev = " ".join(reversed(st))
    return rev


if __name__ == "__main__":

    # input_str = "the sky is blue"   # output: "blue is sky the"
    # input_str = "  hello world!  "   # output: "world! hello"
    input_str = "a good   example"   # output: "example good a"
    print(reverse_words(input_str))
