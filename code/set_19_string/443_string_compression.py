# String Compression
# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.
# After you are done modifying the input array in-place, return the new length of the array.

# Follow up:
# Could you solve it using only O(1) extra space?

# Example 1:
# Input:
# ["a","a","b","b","c","c","c"]
# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

# Example 2:
# Input:
# ["a"]
# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]
# Explanation:
# Nothing is replaced.

# Example 3:
# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output:
# Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
# Notice each digit has it's own entry in the array.

# Note:
# All characters have an ASCII value in [35, 126].
# 1 <= len(chars) <= 1000.
# ========================================================================================
# Algorithm:
# TC:
# SC:
# ========================================================================================


def compress(chars):

    if len(chars) == 0:
        return None

    idx = 0
    i = 0

    while i < len(chars):
        chars[idx] = chars[i]
        idx += 1
        j = i
        while j < len(chars) and chars[j] == chars[i]:
            j += 1

        if j - i > 1:
            count = str(j-i) + ""
            for c in count:
                chars[idx] = c
                idx += 1

        i = j

    return idx


if __name__ == "__main__":

    input_str = ["a", "a", "b", "b", "c", "c", "c"]    # output: 6
    # input_str = ["a"]    # output: 1
    # input_str = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]  # output: 4
    print(compress(input_str))
