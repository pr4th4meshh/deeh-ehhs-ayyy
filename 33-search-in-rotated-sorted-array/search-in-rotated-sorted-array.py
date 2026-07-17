class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (r + l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            
        pivot = l

        def bSearch(l: int, r: int) -> int:
            while l <= r:
                mid = (r + l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        res = bSearch(0, pivot - 1)
        if res != -1:
            return res

        return bSearch(pivot, len(nums) - 1)