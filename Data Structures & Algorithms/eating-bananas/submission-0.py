import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        
        output = high
        while low <= high:
            mid = low + (high-low)//2

            this_h = 0
            for pile in piles:
                if pile <= mid:
                    this_h += 1
                else:
                    this_h += math.ceil(pile / mid)
                    
                
                if this_h > h:
                    break
            
            if this_h <= h:
                output = min(output, mid)
                high = mid - 1
            else:
                low = mid + 1

            
        return output


