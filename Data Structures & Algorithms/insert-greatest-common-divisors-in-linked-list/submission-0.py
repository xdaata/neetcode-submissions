# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        head2 = head.next
        while head and head2:
            curr_val = head.val
            next_val = head2.val

            nxt = head.next
            head.next = ListNode(math.gcd(curr_val, next_val))
            head = head.next
            head.next = nxt

            head = head.next
            head2 = head2.next

        return dummy.next          

