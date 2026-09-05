"""
Koko Eating Bananas
Medium

You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Constraints:

1 <= piles.length <= 1,000
piles.length <= h <= 1,000,000
1 <= piles[i] <= 1,000,000,000

https://neetcode.io/problems/eating-bananas/question?list=neetcode150
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        k is the number of bananas you can eat during 1 hour.
        This is speed of eating bananas.
        you have to return minimum k.
        maybe you can use binary search algorithm,
        you look minimum k between left and right pointers.

        piles.length <= h <= 1,000,000
        -> maximum k is max(piles). Because if k is max(piles), you take only len(piles) hours.
        ex. piles = [25,10,23,4], max(piles)=25, len(piles)=4, if k is 25, you only take 4 hours.
        That's why k is moving between 1 to max(piles).
        k couldn't be over max(piles) because that's all true if k is over max(piles).
        """
        l, r = 1, max(piles)
        while l <= r:
            mid = l + ((r - l) // 2)
            if self.canEatAllBananas(piles, h, mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
    
    def canEatAllBananas(self, piles: List[int], h: int, k: int) -> bool:
        hours = 0
        for b in piles:
            hours += b // k
            if b % k != 0:
                hours += 1
            if hours > h:
                return False
        return hours <= h