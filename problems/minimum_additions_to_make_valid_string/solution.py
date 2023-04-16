class Solution:
    def addMinimum(self, word: str) -> int:
        # edge case at front and end
        count = ord(word[0]) - ord('a')
        print(word[0], count)
        for i in range(0, len(word)-1):
            cur, nxt = word[i], word[i+1]
            if cur == 'b':
                if nxt == 'a':
                    count += 1
                elif nxt == 'b':
                    count += 2
                elif nxt == 'c':
                    count += 0
            elif cur == 'c':
                if nxt == 'a':
                    count += 0
                elif nxt == 'b':
                    count += 1
                elif nxt == 'c':
                    count += 2
            elif cur == 'a':
                if nxt == 'a':
                    count += 2
                elif nxt == 'b':
                    count += 0
                elif nxt == 'c':
                    count += 1
            print(word[i], count)
        count += ord('c') - ord(word[-1])
        print(word[-1], count)
        return count