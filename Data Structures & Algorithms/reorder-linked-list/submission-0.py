# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        l1 = head
        l2 = head.next
        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next

        prev = None
        curr = l1.next
        l1.next = None
        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt

        first_half = head
        second_half = prev

        while second_half:
            tmp1 = first_half.next
            tmp2 = second_half.next

            first_half.next = second_half
            second_half.next = tmp1

            first_half = tmp1
            second_half = tmp2



        

        