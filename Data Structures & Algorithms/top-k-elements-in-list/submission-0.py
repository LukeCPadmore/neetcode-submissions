from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] +=1
        
        sorted_freq = sorted(freq.items(),key = lambda x:x[1], reverse = True)
        print(sorted_freq)

        return [k for k,v in sorted_freq[:k]]
        