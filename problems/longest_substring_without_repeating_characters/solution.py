class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        
        cur_str = ""
        cur_set = set()
        
        for candidate in s:
            while candidate in cur_set:
                cur_set.remove(cur_str[0])
                cur_str = cur_str[1:]
            
            cur_str += candidate
            cur_set.add(candidate)
            cur_len = len(cur_str)
            
            if cur_len > max_len:
                max_len = cur_len
        return max_len
                
            
            
            
        