import heapq as pq 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-x for x in stones]
        pq.heapify(q)
        while len(q) > 1:
            s1 = -pq.heappop(q)
            s2 = -pq.heappop(q)
            pq.heappush(q,s2-s1)
        if q:
            return -q[0]
        else:
            return 0
        