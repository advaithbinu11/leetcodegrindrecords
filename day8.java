class Solution {
    public int hIndex(int[] citations) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int max = 0;
        for(int num : citations){
            if(map.get(num) == null){
                map.put(num,1);
            }
            else{
                map.put(num, map.get(num)+1);
            }
            if(num>max){
                max = num;
            }
        }
        int[] arr = new int[max+1];
        arr[arr.length-1] = map.get(max);
        if(arr[arr.length-1]>=arr.length-1){
            return arr.length-1;
        }
        for(int i = arr.length-2;i>=0;i--){
            int val = 0;
            if(map.get(i)!=null){
                val = map.get(i);
            }
            arr[i] = val+arr[i+1];
            if(arr[i]>=i){
                return i;
            }
        }
        return 1;
    }
}
