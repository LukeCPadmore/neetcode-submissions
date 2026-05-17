class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1
        while True:
            print(l,r)
            if target == numbers[l] + numbers[r]:
                return [l+1,r+1]
            if target < numbers[l] + numbers[r]:
                r-=1
            if target > numbers[l] + numbers[r]:
                l+=1
            
        
        