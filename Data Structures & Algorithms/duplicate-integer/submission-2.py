class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        y = len(nums)
        nums= set(nums)
        if len(nums) == y:
            return true
        else:
            return false