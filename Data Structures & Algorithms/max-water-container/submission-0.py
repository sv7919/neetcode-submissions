class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        thoughts: find the largest number and determine if it is bigger than the previous number checked, then compare it to the pointer on the other side which is n indexes away
        '''

        i = 0
        j = len(heights) - 1 # width
        w = j - i
        best_area = 0

        while i < j:
            h = min(heights[i], heights[j])
            w = j - i
            curr_area = w * h
            
            if curr_area > best_area:
                best_area = curr_area
            if heights[i] <= heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
        
        return best_area
