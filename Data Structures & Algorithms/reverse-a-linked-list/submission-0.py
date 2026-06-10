# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # reversed_list = None
        # temp = ListNode(0,None)
        # while head.next is not None:
        #     temp.val = head.next
        #     head = head.next
        #     head.next.val = temp.val
        # return head


##################

        prev = None
        curr = head
            
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
            