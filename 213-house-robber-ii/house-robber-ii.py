class Solution:
    def rob(self, nums: List[int]) -> int:
        #TC = O(n) because it depends on input size
        #SC = O(n) because declaring vars in helper function and 
        #slicing the nums array
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
        # [rob1, n, rob2, n+1, n+2, ..]
    def helper(self, nums):
        rob1 = rob2 = 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2