/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null){
            return list2;
        }
        if (list2 == null){
            return list1;
        }
        if(list1.val > list2.val){
            ListNode temp = list1;
            list1 = list2;
            list2 = temp;
        }
        return helper(list1, list2);
    }
    public ListNode helper(ListNode list1, ListNode list2) {
        if (list2 == null) {
            return null;
        }
        if (list1.val == list2.val) {
            ListNode newL2 = list2.next;
            list2.next = list1.next;
            list1.next = list2;
            list2 = newL2;
            helper(list1, list2);
            return list1;
        }
        else {
            int nextVal = list1.next == null ? 101 : list1.next.val;
            if (nextVal > list2.val) {
                ListNode newL2 = list2.next;
                list2.next = list1.next;
                list1.next = list2;
                list2 = newL2;
                helper(list1, list2);
                return list1;  
            }
            else{
                helper(list1.next, list2);
                return list1;  
            }
        }
    }
}
