class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=prices[0]
        for i in range(len(prices)-1):

            if buy<prices[i+1]:
                profit=max(profit,prices[i+1]-buy)

            buy=min(buy,prices[i+1])


        return profit

