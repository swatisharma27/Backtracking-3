class Solution:
    """
    TC: O(m*n*4L); m - rows, n - columns, L - length of the word
    AS: O(L); L - length of the word (one recursive call on each character of the word)
    """

    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0]) 

        # DFS
        def helper(board, r, c, word, idx):

            m = len(board)
            n = len(board[0])
            dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

            # base
            if idx == len(word):
                return True
            # bound check
            if (r < 0 or c < 0 or r == m or c == n):
                return False

            # logic
            if board[r][c] == word[idx]:
                # action
                board[r][c] = "#"
                for dr, dc in dirs:
                    nr = dr + r
                    nc = dc + c
                    # recurse
                    if helper(board, nr, nc, word, idx+1):
                        return True
                # backtrack
                board[r][c] = word[idx]
                return False
                
        for i in range(0, m):
            for j in range(0, n):
                if helper(board, i, j, word, 0):
                    return True
        return False 
    
if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 
    word = "ABCCED"
    sol = Solution()
    print("TEST CASE 1")
    print(sol.exist(board, word))

    print("\n\n")

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    print("TEST CASE 2")
    print(sol.exist(board, word))