class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brac = {")":"(","]":"[","}":"{"}

        for x in s:
            if x in brac:
                if stack and stack[-1] == brac[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        if not stack:
            return True
        else:
            return False
