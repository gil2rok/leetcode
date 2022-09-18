class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        max_len = 1
        cur_len = 1
        
        prev = s[0]
        for cur in s[1:]:
            # if cur char alphabetically comes after prev char
            if ord(cur) - ord(prev) == 1:
                cur_len += 1
            else:
                max_len = max(max_len, cur_len)
                cur_len = 1
            prev = cur
        
        return max(max_len, cur_len)