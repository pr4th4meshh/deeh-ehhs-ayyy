class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # LEFT POINTER
        left = 0 
        # RIGHT POINTER
        right = len(numbers) - 1

        # WHILE LEFT POINTER IS LESS THAT RIGHT POINTER
        while left < right:
            # INIT CURRENT SUM AS TOTAL OF FIRST AND LAST ELEMENT IN THE ARRAY
            currSum = numbers[left] + numbers[right]
            if currSum > target:
            # MOVE RIGHT POINTER TO LEFT
                right -= 1
            elif currSum < target:
            # MOVE LEFT POINTER TO RIGHT
                left += 1
            else:
            # ADD + 1 TO INDEX BECAUSE THE numbers ARRAY'S INDEX IS FROM 1
                return[left + 1, right + 1]
        # BASE RETURN EMPTY ARRAY
        return []