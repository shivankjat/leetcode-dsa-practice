class Solution:
    def findMax(self, piles):
        maxi = float("-inf")
        for pile in piles:
            maxi = max(maxi, pile)
        return maxi
    
    def calculateTotalHours(self, piles, hourly):
        totalH = 0
        for pile in piles:
            totalH += math.ceil(pile / hourly)
        return totalH
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = self.findMax(piles)
        while low < high:
            mid = (low + high) // 2
            totalH = self.calculateTotalHours(piles, mid)
            if totalH > h:
                low = mid + 1
            else:
                high = mid
        return low