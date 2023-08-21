class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        first_letter = "".join([word[0] for word in words])
        return first_letter == s
        