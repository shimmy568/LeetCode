import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def extractNum(self, linkl):
        s = 0
        cur = linkl
        i = 0
        while cur != None:
            s += cur.val * (10 ** i)
            i += 1
            cur = cur.next
        return s
    
    def createList(self, num):
        if num == 0:
            return ListNode(0)
        l = []
        n = len(str(num))
        for x in reversed(range(n)):
            d = num // (10 ** x)
            l.append(d)
            
            num -= d * (10 ** x)

        h = None
        cur = None
        for x in reversed(l):
            if h == None:
                h = ListNode(x)
                cur = h
            else:
                cur.next = ListNode(x)
                cur = cur.next
        return h  
            
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = self.extractNum(l1) + self.extractNum(l2)
            
        return self.createList(s)
            