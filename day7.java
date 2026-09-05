/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        while(true){
        if(head == null){
            return false;
        }
        else if(head == head.next){
            return true;
        }
        else{
            ListNode save = head.next;
            head.next = head;
            head = save;
        }
        }
    }
}
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<Integer>> map = new HashMap<String, ArrayList<Integer>>();
        for(int pos = 0; pos<strs.length; pos++){
            String str = strs[pos];
            int[] alpha = new int[26];
            for(int i = 0; i<str.length();i++){
                alpha[(str.charAt(i)-'a')] += 1;
            }
        if(map.get(Arrays.toString(alpha)) == null){
            ArrayList<Integer> indexes = new ArrayList<Integer>();
            indexes.add(pos);
            map.put(Arrays.toString(alpha), indexes);
        }
        else{
            map.get(Arrays.toString(alpha)).add(pos);
        }
        }
        List<List<String>> res = new ArrayList<List<String>>();
        for(String key : map.keySet()){
            ArrayList<String> arr = new ArrayList<String>();
            for(int pos : map.get(key)){
                arr.add(strs[pos]);
            }
            res.add(arr);
        }
        return res;
    }
}
