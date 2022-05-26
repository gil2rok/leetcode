class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        result_dict = {} # {sorted str : [anagram_1 ... anagram_N] }
        for s in strs:
            sorted_s = ''.join(sorted(s))
            cur_list = result_dict.get(sorted_s, [])
            cur_list.append(s)
            result_dict[sorted_s] = cur_list
        
        result_list = []
        for v in result_dict.values():
            result_list.append(v)
            
        return result_list