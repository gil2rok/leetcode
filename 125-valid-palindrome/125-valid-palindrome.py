class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert into lowercase and remove non-alphanumeric characters (letters + numbers)
        s = ''.join(filter(str.isalnum, s.lower()))
        
        p1 = 0 # pointer 1
        p2 = len(s) - 1 # pointer 2
        
        while p1 < p2: # while two pointers have not met up
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
            
        return True