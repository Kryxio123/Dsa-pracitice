class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while right> 0 and left < len(numbers):
            sum = numbers[right] + numbers[left]
            if sum == target:
                return [left+1,right+1]
            elif sum > target:
                right -=1
            elif sum < target:
                left +=1

        