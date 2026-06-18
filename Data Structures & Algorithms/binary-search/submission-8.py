class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            print(f'left={l}, right={r}, mid={m}')
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else: 
                r = m 
        return -1
