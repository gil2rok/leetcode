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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l = 0; r = len(height) - 1
#         max_area = 0
        
#         while l < r: # while pointers haven't met yet
#             area = self.compute_area(height, l, r)
#             max_area = max(area, max_area)
            
#             if height[l] > height[r]:
#                 r-= 1
#             else:
#                 l += 1
#         return max_area
        
#     def compute_area(self, height, l, r):
#         h = min(height[l], height[r])
#         w = r - l
#         return h * w
    
    