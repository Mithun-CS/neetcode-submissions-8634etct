import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right = 1 , max(piles)
        
        while left < right:
            mid_speed = left +(right - left)//2

            total_hours = sum(math.ceil(i/mid_speed) for i in piles)
            if total_hours <= h:
                right = mid_speed
            else:
                left = mid_speed + 1
        return left