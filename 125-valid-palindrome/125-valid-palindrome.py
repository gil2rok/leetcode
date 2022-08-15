class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert into lowercase and remove non-alphanumeric characters (letters + numbers)
        #s = ''.join(filter(str.isalnum, s.lower()))
        
        l = 0 # pointer 1
        r = len(s) - 1 # pointer 2
        
        while l < r: # while two pointers have not met up
            while l<r and not self.isalphanum(s[l]):
                l += 1
            while r>l and not self.isalphanum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
            
        return True
    
    def isalphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))