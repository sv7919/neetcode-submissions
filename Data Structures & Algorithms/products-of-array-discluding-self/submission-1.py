class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use division to calculate the total product and then just 
        # divide by nums[i]

        if nums.count(0) >= 2:
            return [0] * len(nums)
        elif nums.count(0) == 1:
            i = nums.index(0)
            del nums[i]
            prod = 1
            for j in range(len(nums)):
                prod *= nums[j]
                nums[j] = 0
            nums.insert(i, prod)
            return nums
        else:
            prod = 1
            for i in range(len(nums)):
                prod *= nums[i]
            
            res = [prod//nums[i] for i in range(len(nums))]
            return res

