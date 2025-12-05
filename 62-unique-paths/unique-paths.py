class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        arr = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                print(arr)
                if i == 0 or j == 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i][j-1] + arr[i-1][j]

        
        return arr[i][j]



