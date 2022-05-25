class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        for s_char in s:
            if s_char in t:
                t = t.replace(s_char, '', 1)
            else:
                return False
        
        if t == '':
            return True
        else:
            return False
        