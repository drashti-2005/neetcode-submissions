# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists)>1:
            mergedList=[]
            for i in range(0,len(lists),2):
                list1=lists[i]
                if i+1<len(lists):
                    list2=lists[i+1]
                else:
                    list2=None
                mergedList.append(self.mergeList(list1,list2))
            lists=mergedList
        return lists[0]
    def mergeList(self,list1,list2):
        d=ListNode()
        curr=d
        while list1 and list2:
            if list1.val<list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next
        if list1:
            curr.next=list1
        if list2:
            curr.next=list2
        return d.next

     