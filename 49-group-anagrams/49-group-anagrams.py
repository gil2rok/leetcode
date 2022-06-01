from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ##### SOL 1 #####
        anagrams = dict()
        
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            
            cur_list = anagrams.get(tuple(counts), [])
            cur_list.append(s)
            anagrams[tuple(counts)] = cur_list
            
        return anagrams.values()
        
        
        ##### SOL 2 #####
        # strs = [str_1 ... str_N]
        # Runtime: O(n*m), w/ m = |str|*log(|str|)
        # Memory: O(n)
        
        result_dict = {} # {sorted str : [anagram_1 ... anagram_N] }
        for s in strs:
            # get current anagram list
            sorted_s = ''.join(sorted(s))
            cur_list = result_dict.get(sorted_s, [])
            
            # add s to anagram list
            cur_list.append(s)
            result_dict[sorted_s] = cur_list
        
        result_list = []
        for v in result_dict.values():
            result_list.append(v)
            
        return result_list
        