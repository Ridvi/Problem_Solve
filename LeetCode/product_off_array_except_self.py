class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        for i in range(1,len(nums)):
            ans[i]=ans[i-1]*nums[i-1]

        suffix=1
        for i in range(len(nums)-2,-1,-1):
            suffix = suffix * nums[i+1]
            ans[i]=ans[i]*suffix


        return ans
            
