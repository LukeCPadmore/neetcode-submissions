class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {nums[i]:i for i in range(len(nums))}
        for j in range(0,len(nums)):
            if target - nums[j] in d and d[target - nums[j]] != j:
                return [j,d[target - nums[j]]]