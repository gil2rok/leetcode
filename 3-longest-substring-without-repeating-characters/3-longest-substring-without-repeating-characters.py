class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        unique_chars = set()
        cur_len = 0
        l, r, = 0, 1
        
        while r <= len(s):        
            new_char = s[r-1]
            while new_char in unique_chars:
                unique_chars.remove(s[l])
                l += 1
             
            unique_chars.add(new_char)
            max_len = max(max_len, len(s[l:r]))
            r += 1
        return max_len
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         max_len = 0
        
#         cur_str = ""
#         cur_set = set()
        
#         for candidate in s:
#             while candidate in cur_set:
#                 cur_set.remove(cur_str[0])
#                 cur_str = cur_str[1:]
            
#             cur_str += candidate
#             cur_set.add(candidate)
#             cur_len = len(cur_str)
            
#             if cur_len > max_len:
#                 max_len = cur_len
#         return max_len
                
            
            
            
        