class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l != r:
            total = numbers[l] + numbers[r]
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if total < target:
                l+=1
            if total > target:
                r-=1
        