class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix
        # get the product of all elements before and after an index
        # pre compute two arrays

        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        pref[0] = 1
        suff[n-1] = 1

        # find the prefix array
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]

        # find the suffix array
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]

        # iterate through and multiply the corresponding prefixes and suffixes
        res = [pref[i]*suff[i] for i in range(n)]

        return res