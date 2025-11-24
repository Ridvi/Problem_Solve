class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cumsum=0
        maxsum= nums[0]
        for i in nums:
            cumsum+=i
            maxsum=max(maxsum,cumsum)
            if(cumsum<0):
                cumsum=0

        return maxsum



        
