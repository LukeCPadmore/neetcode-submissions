class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        for i,target in enumerate(nums):
            l, r = 0, len(nums) - 1 
            while l < r:
                s = nums[l] + nums[i] + nums[r]
                if s == 0 and l != i and r != i:
                    res.add(tuple(sorted([nums[l],nums[i],nums[r]])))
                    l+=1
                    continue
                if s < 0 or l == i:
                    l += 1
                if s > 0 or r == i:
                    r -=1 
        return [*res]
            