import heapq as pq 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(x1**2+x2**2,i) for i,(x1,x2) in enumerate(points)]
        pq.heapify(distances)

        ans = []
        for i in range(0,k):
            dist, index = pq.heappop(distances)
            ans.append(points[index])
        
        return ans

        