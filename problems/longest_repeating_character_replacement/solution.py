from heapq import heapify

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0 # len of max substr that contains repeating letter after k transformations
        l, r = 0, 1
        counts = collections.defaultdict(int) # dict[char] = count
        majority_count = 0 # num times majority char appears in cur substr
        
        for r in range(len(s)):
            new_char = s[r]
            counts[new_char] += 1
            majority_count = max(majority_count, counts[new_char])

            # while cannot transform cur str into a 1-letter substring with k replacements
            while majority_count + k < len(s[l:r+1]):
                counts[s[l]] -= 1 # decrement count dict
                
                majority_count -= 1
                for v in counts.values():
                    majority_count = max(majority_count, v)
               
                #majority_count = max(list(counts.values()).append(majority_count - 1))
                l += 1
            max_len = max(max_len, len(s[l:r+1]))
        return max_len
        
        
        
        
        
        
        
        
        
        
#         max_len = 0 # len of max substr that contains repeating letter after k transformations
#         l, r = 0, 1
#         counts = collections.defaultdict(int) # dict[char] = count
#         #heap = [] # heap for tuples (char count, char)

#         #majority_char = "" # majority char within cur substr
#         majority_count = 0 # num times majority char appears in cur substr

#         while r <= len(s):
#             new_char = s[r-1]
#             counts[new_char] += 1

#             #new_tuple = (-counts[new_char], new_char) # negate count to implement max heap
#             #heap.append(new_tuple).heappush # add element to heap in O(1)

#             # update majority values
#             majority_count = max(majority_count, counts[new_char])

#             #if counts[new_char] > majority_count:
#             #    majority_count = counts[new_char]
#             #    #majority_char = new_char

#             # while cannot transform cur str into a 1-letter substring with k replacements
#             while majority_count + k < len(s[l:r]):
#                 counts[s[l]] -= 1 # decrement count dict

#                 majority_count = 0
#                 for k, v in counts.items():
#                     majority_count = max(majority_count, v)

#                 #updated_tuple = (-counts[s[l]], s[l])
#                 #heap.heappushpop(updated_tuple) # update heap

#                 l += 1

#             max_len = max(max_len, len(s[l:r]))

#         return max_len