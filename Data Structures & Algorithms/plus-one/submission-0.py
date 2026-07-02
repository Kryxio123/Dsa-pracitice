class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newStr =""
        res=[]
        for x in digits:
            newStr += str(x)
        newStr = int(newStr) + 1
        for y in str(newStr):
            res.append(int(y))
        return res