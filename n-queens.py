class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        """
        TC : O(n^n) or O(n!)
        AS: O(n*n) ; n rows and n columns
        """

        # create a matrix for the board with all elements set to False
        result = []
        board = [[False for _ in range(n)]for _ in range(n)]

        def helper(board, r):
            n = len(board)

            # base case
            if r == n:
                li = []
                for i in range(0, n):
                    sb = ""
                    for j in range(0, n):
                        if board[i][j] == True:
                            sb += "Q"
                        else:
                            sb += "."
                    li.append(sb)
                result.append(li)

            
            # logic
            for c in range(0, n): 
                if isSafe(board, r, c):
                    ## ACTION
                    board[r][c] = True
                    ## RECURSE
                    helper(board, r+1)
                    ## BACKTRACK
                    board[r][c] = False

        def isSafe(board, r, c):
            n = len(board)

            # Column Up
            for i in range(0, r):
                if board[i][c]:
                    return False

            # up left diagonal
            i = r
            j = c
            while (i >= 0 and j >= 0):
                if board[i][j]:
                    return False
                i -= 1
                j -= 1

            # up right diagonal
            i = r
            j = c
            while (i >= 0 and j <n):
                if board[i][j]:
                    return False
                i -= 1
                j += 1

            return True

        helper(board, 0)
        return result


if __name__ == "__main__":
    n = 4
    sol = Solution()
    print("TEST CASE 1")
    print(sol.solveNQueens(n))

    print("\n\n")

    n1 = 1
    print("TEST CASE 2")
    print(sol.solveNQueens(n1))