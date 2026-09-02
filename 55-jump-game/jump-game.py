class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # solve w backward greedy
        goal = len(nums) - 1 # last index of nums

        for i in range(len(nums) - 2, -1 , -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0