class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        s = 1
        while s:
            sum = 0
            while n>0:
                val = n%10
                sum += val**2
                n//=10
            if sum == 1:
                return True
            n = sum
            if sum not in check:
                check.add(sum)
            elif sum in check:
                return False
