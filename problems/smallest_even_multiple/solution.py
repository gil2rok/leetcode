class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0: # if n is even
            return n
        else:
            return 2 * n