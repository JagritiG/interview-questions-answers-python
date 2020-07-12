# Valid palindrome
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: "race a car"
# Output: false

# Constraints:
# s consists only of printable ASCII characters.
# ======================================================================================
# Algorithm:
# TC: O(n)
# SC: O(1)
# ========================================================================================


def is_palindrome(s):

    if len(s) == 0:
        return None

    left = 0
    right = len(s) - 1

    while left < right:

        if not s[left].isalpha() and not s[left].isdigit():
            left += 1

        elif not s[right].isalpha() and not s[right].isdigit():
            right -= 1

        else:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

    return True


if __name__ == "__main__":

    # input_str = "A man, a plan, a canal: Panama"   # output: True
    input_str = "race a car"   # output: False
    print(is_palindrome(input_str))
