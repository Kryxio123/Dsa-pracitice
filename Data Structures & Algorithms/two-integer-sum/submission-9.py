class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Difference= {}
        for x in range(len(nums)):
            diff = target - nums[x]
            if nums[x] in Difference:
                print(diff,Difference,Difference.get(nums[x],0))
                prevIndex = Difference.get(nums[x],0)
                return [prevIndex,x] 
            Difference[diff] = x

