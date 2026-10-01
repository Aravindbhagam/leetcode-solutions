class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            b = target-num
            if b in seen:
                return(seen[b],i)
            seen[num]=i
