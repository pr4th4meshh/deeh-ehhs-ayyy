class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # Base condition
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    """Skip the rest of the loop and 
                    continue with the next iteration."""
                    continue

                """ Initialize variables to store the number
                of ways from cell above (up) and left (left)"""
                up = 0
                left = 0

                """ If we are not at first row (i > 0), update 
                'up' with the value from the cell above"""
                if i > 0:
                    up = dp[i - 1][j]

                """ If we are not at the first column (j > 0),
                update 'left' with value from the cell to left"""
                if j > 0:
                    left = dp[i][j - 1]

                """ Calculate the number of ways to reach the
                current cell by adding 'up' and 'left'"""
                dp[i][j] = up + left

        # The result is stored in bottom-right cell (m-1, n-1)
        return dp[m - 1][n - 1]



