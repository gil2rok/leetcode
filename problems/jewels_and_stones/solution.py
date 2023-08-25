class Solution:
    """
    n = len(jewels) m = len(stones) n' = len(set(jewels))
    Time:   O(nm)
    Space:  O(n')
    """
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_dict = {jewel: idx for idx, jewel in enumerate(jewels)}
        count = 0
        for stone in stones:
            if stone in jewel_dict:
                count += 1
        return count