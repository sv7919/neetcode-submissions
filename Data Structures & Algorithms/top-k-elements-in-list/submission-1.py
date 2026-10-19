from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
# gets the value at a specified key at num, the zero is error handling
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if  len(heap) > k:
                heapq.heappop(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result