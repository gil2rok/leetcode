class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [None] * len(pref)
        
        arr[0] = pref[0]
        for i, (p1, p2) in enumerate(zip(pref[:-1], pref[1:])):
            p1_bin, p2_bin = self.convert(p1, p2)
            
            arr_bin = ""
            #print(p1_bin, p2_bin)
            for b1, b2 in zip(p1_bin, p2_bin):
                if b2 == '0':
                    arr_bin += b1
                elif b2 == '1':
                    if b1 == '0': arr_bin += '1'
                    elif b1 == '1': arr_bin += '0'
                #print(b1, b2, arr_bin[-1])
            arr[i+1] = int(arr_bin, 2)
        return arr
            
    def convert(self, p1, p2):
        p1_bin = bin(p1)[2:]
        p2_bin = bin(p2)[2:]

        max_len = max(len(p1_bin), len(p2_bin))
        p1_bin = '0' * (max_len - len(p1_bin)) + p1_bin
        p2_bin = '0' * (max_len - len(p2_bin)) + p2_bin
        return p1_bin, p2_bin