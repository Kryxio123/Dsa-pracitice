class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for digit in range(len(nums)):
            difference = target - nums[digit]
            if map.get(difference) != None:
                return [map.get(difference),digit]
            map[nums[digit]] = digit
            