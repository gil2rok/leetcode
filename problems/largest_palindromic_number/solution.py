class Solution:
    def largestPalindromic(self, num: str) -> str:
        num = list(map(int, num))
        res = []
        
        count = [0] * 10
        for n in num:
            count[n] += 1
        
        for i in range(len(count)-1, -1, -1):
            if i == 0 and len(res) == 0:
                break
                
            while count[i] >= 2:
                res.append(str(i))
                count[i] -= 2
                
        even_len = len(res)
        
        for i in range(len(count) - 1, -1 , -1):
            if count[i] >= 1:
                res.append(str(i))
                break
        
        for i in range(even_len - 1, -1, -1):
            res.append(res[i])
            

        return ''.join(res)
        
        