class Solution:
    def rob(self, nums: List[int]) -> int:
        #TC = O(n) because depends on input
        #SC = O(1) because we defined variables
        rob1, rob2 = 0, 0

        # [rob1, n, rob2, n + 1, n + 2, ...]
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
