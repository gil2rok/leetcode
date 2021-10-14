class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0; r = len(height) - 1
        max_area = 0
        
        while l < r: # while pointers haven't met yet
            area = self.compute_area(height, l, r)
            max_area = max(area, max_area)
            
            if height[l] > height[r]:
                r-= 1
            else:
                l += 1
        return max_area
        
    def compute_area(self, height, l, r):
        h = min(height[l], height[r])
        w = r - l
        return h * w
    
    