class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = []
        for n in nums:
            if n not in check:
                check.append(n)
            else:
                return True
        return False
        