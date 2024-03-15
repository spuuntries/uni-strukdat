class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        res = []
        for i, p in enumerate(prices):
            lowestPrice = 0
            for d in prices[i+1:]:
                if d <= p:
                   lowestPrice = d
                   break
            res.append(p-lowestPrice)
        return res