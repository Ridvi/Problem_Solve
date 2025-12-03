class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = (start + end) // 2
            
            # Ensure mid is even
            if mid % 2 == 1:
                mid -= 1

            # If pair matches, answer is on the right
            if nums[mid] == nums[mid + 1]:
                start = mid + 2
            else:
                end = mid

        return nums[start]



#(1,1)(2,2)(3,3)
#all are in pair if one is different it will break the pair
#(1,1)(2,5)(3,3)
