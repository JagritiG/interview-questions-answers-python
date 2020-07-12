# Reverse String
# Write a function that reverses a string.
# The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this
# by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.

# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
# ========================================================================================
# Algorithm:
# TC: O(n)
# SC: O(1)
# ========================================================================================


def reverse_string(s):

    if len(s) == 0:
        return None

    if len(s) == 1:
        return s[0]

    left = 0
    right = len(s)-1

    while left < len(s)//2:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s


if __name__ == "__main__":

    # input_str = ["h","e","l","l","o"]    # output: ["o","l","l","e","h"]
    input_str = ["H", "a", "n", "n", "a", "h"]    # output: ["h","a","n","n","a","H"]
    # input_str = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
    # output : ["a", "m", "a", "n", "a", "P", " ", ":", "l", "a", "n", "a", "c", " ", "a", " ", ",", "n", "a", "l", "p", " ", "a", " ", ",", "n", "a", "m", " ", "A"]
    #          ['a', 'm', 'a', 'n', 'a', 'P', ' ', ':', 'l', 'a', 'n', 'a', 'c', ' ', 'a', ' ', ',', 'n', 'a', 'l', 'p', ' ', 'a', ' ', ',', 'n', 'a', 'm', ' ', 'A']
    print(reverse_string(input_str))
