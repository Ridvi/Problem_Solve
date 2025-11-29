class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea=0
        l=0
        r=len(height)-1
        while(l<r):
            w=r-l
            h=min(height[l],height[r])
            current=w*h
            maxarea=max(current,maxarea)
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return maxarea
