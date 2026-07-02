class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0 or len(s) == 1:
            return s
        maxOdd = ""
        maxEven = ""
        for x in range(1,len(s)):
            l = x - 1
            r = x + 1
            palin =""
            palin +=s[x]
            check = True
            while check:
                if l < 0 or r >= len(s):
                    check = False
                elif s[l] == s[r]:
                    palin = s[l] + palin + s[r]
                else:
                    check = False
                l -=1
                r +=1
            maxOdd = max(maxOdd,palin, key = len)
            print(maxOdd)


        for y in range(1,len(s)):
            if s[y] == s[y-1]:
                l = y-2
                r = y+1
                palin = s[y-1] + s[y]
                check = True
                while check:
                    if l < 0 or r >= len(s):
                        check = False
                    elif s[l] == s[r]:
                        palin = s[l] + palin + s[r]
                    else:
                        check = False
                    l -=1
                    r +=1
                maxEven = max(maxEven,palin, key = len)
                print(maxEven)
        return max(maxEven,maxOdd, key=len)
                    