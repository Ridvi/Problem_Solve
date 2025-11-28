class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq=0
        for i in nums:
            if freq==0:
                ans=i
            if ans==i:
                freq= freq+1
            else:
                freq = freq -1
        return ans

#moores voting algo
