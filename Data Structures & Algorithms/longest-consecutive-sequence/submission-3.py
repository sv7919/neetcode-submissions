class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Initial Thoughts:
        I can take the array and use .sort() to make sure it is sorted 
        in ascending order. Now I can start with the first number as I 
        know it is the smallest one and begin counting. I could possibly 
        implement a sort of linkedlist design but that might be 
        overcomplicating it. If iterate by the index, I can check the 
        difference by accessing the next element: if the difference is
        equal to 1, I'll add 1 to a combo variable, but if it is greater than
        1, reset the combo variable. If the difference is
        0, then continue to loop and nothing is added to combo

        Potential Issues: 
        - the worst time complexity of .sort() is O(nlogn) and the
        algorithm requires that solutions must be in O(n) time.
        '''

        combo_list = []
        curr_combo = 0
        nums.sort()
        #print(nums)

        if nums:
            curr_combo += 1
            for i in range(len(nums)-1):
                diff = nums[i+1]-nums[i]
                # print(diff, nums[i], nums[i+1], curr_combo)
                if diff > 1:
                    # print('combo reset')
                    combo_list.append(curr_combo)
                    curr_combo = 1
                elif diff == 0:
                    continue
                else: # diff equals 1
                    curr_combo += 1
            combo_list.append(curr_combo)
            
        if combo_list:
            return max(combo_list)
        else:
            return curr_combo


        

    