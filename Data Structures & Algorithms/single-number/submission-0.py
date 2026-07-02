class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for x in nums:
            count[x]+=1
        for a,b in count.items():
            if b == 1:
                return a
        