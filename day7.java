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
