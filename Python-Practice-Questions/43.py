# Container with most water.

def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        lp = 0
        rp = len(height) - 1

        while(lp < rp):
            width = rp - lp
            ht = min(height[lp], height[rp])
            max_water = max(max_water, width * ht)

            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1
        
        return max_water