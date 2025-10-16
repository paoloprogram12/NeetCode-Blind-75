from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l_p = 0 # buy
        r_p = 1 # sell
        maxP = 0

        while r_p < len(prices):
            if prices[l_p] < prices[r_p]:
                profit = prices[r_p] - prices[l_p]
                maxP = max(maxP, profit) # assigns new profit to the new max profit
            else:
                l_p = r_p
            r_p += 1
        return maxP
        
def main():
    prices = [10 ,1, 5, 6, 7, 1] # buy at prices[1] = 1 sell at prices[4] = 7
    fort = Solution()
    nite = fort.maxProfit(prices)
    print(nite)

if __name__ == "__main__":
    main()