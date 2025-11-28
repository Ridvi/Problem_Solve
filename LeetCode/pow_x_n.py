class Solution:
    def myPow(self, x: float, n: int) -> float:
        bin=n
        ans=1
        if n<0:
            x=1/x
            bin=-bin
        while bin>0:
            if(bin%2==1):
                ans=ans*x
            x=x*x
            bin=bin/2

        return ans
