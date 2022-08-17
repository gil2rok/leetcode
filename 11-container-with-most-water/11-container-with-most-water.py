class Solution:
    def maxArea(self, height: List[int]) -> int:
        largest_area = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            cur_area = self.compute_area(l, r, height)
            largest_area = max(largest_area, cur_area)
            
            if height[l] >= height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
        return largest_area
        
    def compute_area(self, i, j , height):
        assert(i < j)
        return (j-i) * min(height[i], height[j])
    