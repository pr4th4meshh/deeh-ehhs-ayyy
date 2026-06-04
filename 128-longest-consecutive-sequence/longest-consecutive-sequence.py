class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #create a set
        numberSet = set(nums)
        longest = 0

        # iterate through every element in nums array
        for n in numberSet:
            # check if its start of the sequence
            if (n-1) not in numberSet: # here (n - 1) means checking its neighbour on left
                length = 0
                # while there's consecutive elemtns keep adding +1 to sequence
                while(n + length) in numberSet:
                    length += 1
                # decide longest between len or longest
                longest = max(length, longest)
        return longest