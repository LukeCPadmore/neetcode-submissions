import heapq as pq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = nums
        pq.heapify(self.q)
        self.k = k
        while len(self.q) > k:
            pq.heappop(self.q)
            
    def add(self, val: int) -> int:
        pq.heappush(self.q,val)
        if len(self.q) > self.k:
            pq.heappop(self.q)
        return self.q[0]
        
