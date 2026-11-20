class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        the array isn't sorted
        the allowed time complexity is O(n^2)
        set pointers for a number and set the other two to check for the negative sum
        of that number if it exists
        We can sort the algorithm though to make it easier
        '''

        solutions = []
        nums.sort()
        print(nums)
        for i in range(len(nums)-1, 1, -1):
            target = nums[i]

            j = 0
            k = i - 1
            while j < k:
                left_sum = nums[j] + nums[k]
                if left_sum == -target:
                    sol = sorted([nums[i], nums[j], nums[k]])
                    if sol not in solutions:
                        solutions.append(sol)
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif left_sum > -target:
                    k -= 1
                elif left_sum < -target:
                    j += 1
        
        return solutions