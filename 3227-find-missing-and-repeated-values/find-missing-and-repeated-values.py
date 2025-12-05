class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        flat = [x for row in grid for x in row]
        repeating, missing = -1, -1
        n = len(flat)
        grid_bool = [0 for _ in range(n)]
        for element in flat:
                if element == grid_bool[element-1]:
                    repeating = element
                else:
                    grid_bool[element-1] = element

        for index in range(n):
            if grid_bool[index] == 0:
                missing = index + 1
                break
        
        return [repeating, missing]
