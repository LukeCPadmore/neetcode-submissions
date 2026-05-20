from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1,*[prod(nums[:i]) for i in range(1,len(nums))]]
        suffix = [*[prod(nums[i+1:]) for i in range(len(nums)-1)], 1]
        return[a*b for a,b in zip(prefix,suffix,strict=True)]