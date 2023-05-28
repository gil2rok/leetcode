class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        for i, n in enumerate(reversed(num)):
            if n != str(0):
                break
                
        idx = len(num) - i
        return num[:idx]