class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> arrL = new HashSet<List<Integer>>();
        for(int i = 0; i<nums.length-2; i++){
            int j = i+1;
            int k = nums.length-1;
            int target = -nums[i];
            if(target<0){
                List<List<Integer>> res = new ArrayList<List<Integer>>();
                for(List<Integer> a : arrL){
                    res.add(a);
                }
                return res;
            }
            while(j<k){
                int sum = nums[j] + nums[k];
                if(sum < target){
                    j++;
                }
                else if(sum > target){
                    k--;
                }
                else{
                    ArrayList<Integer> afc = new ArrayList<Integer>();
                    afc.add(nums[i]);
                    afc.add(nums[j]);
                    afc.add(nums[k]);
                    arrL.add(afc);
                    j++;
                }
            }
        }
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        for(List<Integer> a : arrL){
            res.add(a);
        }
        return res;
    }
}
