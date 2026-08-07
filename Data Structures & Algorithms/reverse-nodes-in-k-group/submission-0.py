# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next
        return prev

    def getKth(self, curr, k):
        while curr and k:
            curr = curr.next
            k -= 1
        return curr

    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kth = self.getKth(group_prev, k)
            if not kth:
                break

            group_next = kth.next
            kth.next = None
            group_start = group_prev.next

            new_head = self.reverseList(group_start)

            group_prev.next = new_head
            group_start.next = group_next

            group_prev = group_start


        return dummy.next      