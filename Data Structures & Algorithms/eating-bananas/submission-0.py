import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        mink = r
        while l <= r:
            tot_time = 0
            for p in piles:
                m = (l + r) // 2
                tot_time += math.ceil(p/m)
            if tot_time <= h:
                mink = min(mink, m)
                r = m - 1
            else:
                l = m + 1 
        return mink