class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = dict() # dict[char] = count
        max_len = 0 # len of max substr that contains repeating letter after k transformations
        
        l = 0
        for r in range(len(s)): #O(n)
            counts[s[r]] = 1 + counts.get(s[r], 0)

            # while cannot transform cur str into a str containing only 1 letter using k transformations
            while max(counts.values()) + k < len(s[l:r+1]):
                counts[s[l]] -= 1 # decrement count dict
                l += 1
                
            max_len = max(max_len, len(s[l:r+1]))
        return max_len