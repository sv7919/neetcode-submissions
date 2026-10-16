class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        self.n = len(nums)
        ans = [0] * (2*self.n)
        for i in range(self.n):
            ans[i] = nums[i]
            ans[i + (self.n)] = nums[i]
        return ans