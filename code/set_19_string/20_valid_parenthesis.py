# Valid parenthesis
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:
# Input: "()"
# Output: true

# Example 2:
# Input: "()[]{}"
# Output: true

# Example 3:
# Input: "(]"
# Output: false

# Example 4:
# Input: "([)]"
# Output: false

# Example 5:
# Input: "{[]}"
# Output: true
# ======================================================================================
# Algorithm:
# Stack
# TC:
# SC:
# ========================================================================================


def is_valid(s):
    """Return True if all delimiters are properly match; False otherwise."""

    opening_del = '({['             # opening delimiters
    closing_del = ')}]'             # respective closing delimiters

    stack = []

    for c in s:
        if c in opening_del:
            stack.append(c)           # push opening delimiter on stack
        elif c in closing_del:
            if len(stack) == 0:
                return False        # nothing to match with
            else:
                top = stack.pop()
                if closing_del.index(c) != opening_del.index(top):
                    return False        # mismatched

    if len(stack) == 0:
        return True         # were all symbols matched?


if __name__ == "__main__":

    # input_str = "()"   # True
    # input_str = "()[]{}"   # True
    # input_str = "(]"   # False
    # input_str = "([)]"   # False
    input_str = "{[]}"  # True
    print(is_valid(input_str))
