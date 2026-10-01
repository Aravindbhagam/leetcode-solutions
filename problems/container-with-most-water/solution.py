class Solution:
    def maxArea(self, height: List[int]) -> int:
        water=0
        left=0
        right=len(height)-1
        while (left<right):
            maxw=(right-left)*min(height[left],height[right])
            water=max(water,maxw)
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return water
                

        