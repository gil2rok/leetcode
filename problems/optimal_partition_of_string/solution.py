class Solution:
    def partitionString(self, s: str) -> int:
        num_partitions = 0
        cur = dict()
        
        l, r = 0, 0
        for r in range(len(s)):
            new_char = s[r]
            
            if new_char in cur:  # make new substr
                num_partitions += 1
                l = r
                cur = {new_char : 1}
            else:  # add new_char to cur substr
                cur[new_char] = 1
            
        return num_partitions + (len(cur) != 0)
            
            
            
            