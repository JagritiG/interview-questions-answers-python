# Word search
# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

# Example:
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

# Constraints:
# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
# =====================================================================================
# Concept: DFS
# Algorithm:
# Iterate through each cell of the grid to find the first letter of the target word.
# If finds the first letter of the target word, perform depth first search (dfs) on this cell,
# basically search at neighboring cells for remaining letters of the target word.
# If all the letters or characters found, return True
# Else, return False
# ===========================================================================================
# Time complexity: O(N) where N is the number of cells
# Space complexity: O(N)


def exist(board, word):

    def find_letters(board, i, j, count, word):
        if count == len(word):
            return True

        # Corner check if i or j exceeds boundary or if the current letter is not in word, return False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != word[count]:
            return False

        # Store the current character at temp and mark it as empty string, so that
        # the same letter cell may not be used more than once,
        # and add it back after all the recursive calls.
        temp = board[i][j]
        board[i][j] = ' '

        found = find_letters(board, i+1, j, count+1, word)\
            or find_letters(board, i-1, j, count+1, word)\
            or find_letters(board, i, j+1, count+1, word)\
            or find_letters(board, i, j-1, count+1, word)

        board[i][j] = temp
        return found

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0] and find_letters(board, i, j, 0, word):
                return True

    return False


if __name__ == "__main__":

    input_matrix = [['A', 'B', 'C', 'E'],
                    ['S', 'F', 'C', 'S'],
                    ['A', 'D', 'E', 'E']]

    # target_word = "ABCCED"  # True
    # target_word = "SEE"    # True
    target_word = "ABCB"   # False

    print(exist(input_matrix, target_word))
