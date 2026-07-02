class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        y = len(nums)
        print(y,nums)
        x = set(nums)
        print(x,len(x))
        if len(x) == y:
            return False
        else:
            return True