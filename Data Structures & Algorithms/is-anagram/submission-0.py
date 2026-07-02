class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS,countT = {},{}
        if len(s) != len(t):
            return False
        for letter in range(len(s)):
            countS[s[letter]] = 1 + countS.get(s[letter],0)
            countT[t[letter]] = 1 + countT.get(t[letter],0)
        for char in countS:
            if countS[char] != countT.get(char,0):
                return False
        return True




        