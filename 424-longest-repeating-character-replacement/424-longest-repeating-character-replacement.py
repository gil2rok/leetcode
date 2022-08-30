class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = collections.defaultdict(int) # dict[char] = count
        max_len = 0 # len of max substr that contains repeating letter after k transformations
        
        l = 0
        #majority_count = 0 # num times majority char appears in cur substr
        for r in range(len(s)): #O(n)
            counts[s[r]] += 1
            #majority_count = max(majority_count, counts[s[r]])

            # while cannot transform cur str into a str containing only 1 letter using k transformations
            #while majority_count + k < len(s[l:r+1]):
            while max(counts.values()) + k < len(s[l:r+1]):
                counts[s[l]] -= 1 # decrement count dict
                #majority_count -= 1
                
                # find next majority count in O(26)
                #for v in counts.values():
                #    majority_count = max(majority_count, v)
               
                l += 1
            max_len = max(max_len, len(s[l:r+1]))
        return max_len