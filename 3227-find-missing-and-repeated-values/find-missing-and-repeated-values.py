class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        flat = [x for row in grid for x in row]
        print("flat", flat)
        repeating, missing = -1, -1
        n = len(flat)

        for i in range(1, n+1):
            print("i", i)
            count = flat.count(i)
            print("count", count)

            if count == 2:
                repeating = i
            elif count == 0:
                missing = i

        return [repeating, missing]
            