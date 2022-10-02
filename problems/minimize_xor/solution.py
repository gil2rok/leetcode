class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        x1 = self.binarize(num1)
        x2 = self.binarize(num2)
        
        # count num 'set bits' in num2
        total_ones = 0
        for i in x2:
            if i == '1': total_ones += 1
                
        if len(x1) < total_ones:
            x1 += '0' * (total_ones - len(x1))
                
        print(x1, x2)
        
        # find str 'res' that has min val when XOR'ed with num1
        res = ""
        cur_ones = 0
        for i, c in enumerate(x1):
            # print(res, c)
            # if no more '1's remaining, append '0's
            ## ensure don't have too many '1's ##
            if cur_ones == total_ones:
                res += "0" * (len(x1) - i)
                break
                
            # if need to still use z '1's but string can 
            # only be z more characters, append '1's
            ## ensure don't have too few '1's ##
            if len(x1) - i == total_ones - cur_ones:
                res += '1' * (total_ones - cur_ones)
                break
                
            if c == '0':
                res += '0'
            else:
                res += '1'
                cur_ones += 1
                
        # print(res)
        return int(res, 2)               
            
    def binarize(self, num):
        return "{0:b}".format(num)
        