class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for x in range(len(arr)-1,-1,-1):
            if x == len(arr)-1:
                max = arr[x]
                arr[x] = -1
            else:
                tmp = arr[x]
                arr[x] = max
                if max < tmp:
                    max = tmp
        return arr
                      