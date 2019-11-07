class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    a, b = headA, headB
    while a and b:
        if a == b:
            return a
        a = a.next
        b = b.next
        if not a:
            a = headB
        elif not b:
            b = headA
    return None


def judgeIntersectionIfWithCicle(headA, headB):
    def detectCycle(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        f, s = head, head  # fast and slow
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f: break
        if not f or not f.next or not s: return None
        s = head
        while s != f:
            s = s.next
            f = f.next
        return s

    enterPointA, enterPointB = detectCycle(headA), detectCycle(headB)
    if not enterPointA and not enterPointB:  # if both of them don't have a circle
        return getIntersectionNode(headA, headB)

    if enterPointA or enterPointB:  # if one of them has a circle, they won't intersect
        return False

    # if both have circle

    # if they have same enter-circle point
    if enterPointA == enterPointB:
        enterPointA.next = None
        return getIntersectionNode(headA, headB)
    else:
        p = enterPointA.next
        while p != enterPointA:
            if p == enterPointB:
                return enterPointA, enterPointB
            p = p.next
        return None


headA = ListNode(1)
headB = ListNode(1)
a = ListNode(1)
b = ListNode(1)
c = ListNode(1)
d = ListNode(1)
e = ListNode(1)
