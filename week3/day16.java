class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0;
        for(int i = 0; i < height.length; i++){
            for(int k = i + 1; k < height.length; k++){
                int area = (k - i) * Math.min(height[i], height[k]);
                maxArea = Math.max(area, maxArea);
            }
        }
        return maxArea;
    }
}
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while(left < right):
            area = min(height[left], height[right]) * (right - left)
            print(str(left)+" "+str(right)+" "+str(area))
            maxArea = max(area, maxArea)
            if(height[left] < height[right]):
                left+=1
            else:
                right-=1
        return maxArea
        
