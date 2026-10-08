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
