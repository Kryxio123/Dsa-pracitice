class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxi = 0
        for x in numset:
            counter = 0
            if (x-1) not in numset:
                s=x
                
                while s in numset:
                    s+=1
                    counter+=1
            if counter > maxi:
                maxi = counter
        return maxi
