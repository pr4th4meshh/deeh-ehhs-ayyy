class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # solving with backward greedy
        goal = len(nums) - 1 # which is last index of nums
        for i in range(len(nums) -2, - 1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0