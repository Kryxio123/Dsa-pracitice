class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        list1=list(count.most_common(k))
        result = [x[0] for x in list1]
        return result