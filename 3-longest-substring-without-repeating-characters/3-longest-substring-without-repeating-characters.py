class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        unique_chars = set()
        l = 0
        
        for r in range(len(s)):       
            new_char = s[r]
            while new_char in unique_chars:
                unique_chars.remove(s[l])
                l += 1
             
            unique_chars.add(new_char)
            max_len = max(max_len, len(s[l:r+1]))
        return max_len
            
            
            
        