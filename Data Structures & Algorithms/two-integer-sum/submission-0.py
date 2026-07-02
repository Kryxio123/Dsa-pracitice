class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmpList = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] + nums[j] == target) & (i != j):
                    tmpList.append(i)
                    tmpList.append(j)
                    return tmpList                    