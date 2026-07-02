class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterA = {}
        counterB = {}
        if len(s) != len(t):
            return False
        for x in range(len(s)):
            counterA[s[x]] = 1+ counterA.get(s[x],0)
            counterB[t[x]] = 1+ counterB.get(t[x],0)
        
        if counterA == counterB:
            return True
        else:
            return False