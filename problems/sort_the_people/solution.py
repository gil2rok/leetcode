class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_to_name = dict()
        
        for i in range(len(heights)):
            height_to_name[heights[i]] = names[i]
            
        
        for i, h in enumerate(sorted(heights, reverse=True)):
            names[i] = height_to_name[h]
            
        return names