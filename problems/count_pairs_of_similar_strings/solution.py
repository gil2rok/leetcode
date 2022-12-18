class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                char_set1 = set(words[i])
                char_set2 = set(words[j])
                if char_set1 == char_set2:
                    count += 1
                    
        return count