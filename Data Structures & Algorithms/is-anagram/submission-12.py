class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicOne = {}
        dicTwo = {}
        if len(s)!=len(t):
            return False
        for char in s:
            dicOne[char]=dicOne.get(char, 0)+1
        for char in t:
            dicTwo[char]=dicTwo.get(char, 0)+1
        return dicOne==dicTwo

        