class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        
        for i in range(n):
            arr[i] *= arr[i]
        
        l = 0
        r = n - 1
        k = n - 1
        
        while l <= r:
            if arr[l] > arr[r]:
                res[k] = arr[l]
                l += 1
            else:
                res[k] = arr[r]
                r -= 1
            k -= 1
        
        return res