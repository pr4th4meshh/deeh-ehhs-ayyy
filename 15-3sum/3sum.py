class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # Sort to enable two-pointer approach

        for i, a in enumerate(nums):
            # Skip duplicate first elements to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = a + nums[left] + nums[right]

                if total > 0:
                    # Sum is too large, decrease it
                    right -= 1

                elif total < 0:
                    # Sum is too small, increase it
                    left += 1

                else:
                    # Found a valid triplet
                    res.append([a, nums[left], nums[right]])
                    left += 1

                    # Skip duplicate second elements
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res