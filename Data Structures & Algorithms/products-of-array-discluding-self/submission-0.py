class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resi= [1]*len(nums)
        postfix = 1
        prefix = 1
        for x in range(len(nums)):
            resi[x] = prefix
            prefix *= nums[x]
        for y in range(len(nums)-1,-1,-1):
            resi[y] *= postfix
            postfix *= nums[y]
        return resi

        