from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        nums = sorted(nums, key=lambda x: (-count[x], x))
        top_k = []
        for num in nums:
            if len(top_k) == k:
                break
            elif num not in top_k:
                top_k.append(num)
            
        return top_k