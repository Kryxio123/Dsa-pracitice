class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[ ] for i in range(len(nums)+1)]
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        res = []
        for x in range(len(freq)-1 ,0,-1):
            if freq[x] != [] :
                for n in freq[x]:
                    res.append(n)
                    if len(res) == k:
                        return res
        return freq