# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from LinkedList import LinkedList
from stack import Stack
from result import Result


def is_palindrome(head: LinkedList) -> bool:
    reverserd = reverse_and_clone(head)
    return is_equal(head, reverserd)


def reverse_and_clone(node: LinkedList) -> LinkedList:
   head = None
   while node is not None:
       n = LinkedList()
       n.current = node.current
       n.next = head
       head = n
       node = node.next

   return head


def is_equal(one: LinkedList, two: LinkedList)-> bool:
    while one is not None and two is not None:
        if one.current != two.current:
            return False
        one = one.next
        two = two.next
    return one is None and two is None


def isPalinedrome(head: LinkedList):
    fast = head
    slow = head

    stack = Stack()

    while fast is not None and fast.next is not None:
        stack.push(slow.current)
        fast = fast.next.next

    if fast is not None:
        slow = slow.next

    while slow is not None:
        top = int(stack.pop())

        if top != slow.current:
            return False

        slow = slow.next

    return True


def isPalinedromeSecond(head: LinkedList) -> bool:
    length = lengthOfList(head)
    p = isPalinedromeRecurse(head, length)
    return p.result

def isPalinedromeRecurse(head: LinkedList, length: int):
    if head is None and length <= 0:
        return Result(head, True)
    elif length == 1:
        return Result(head.next, True)

    res = isPalinedromeRecurse(head.next, length - 2)

    if res.result is None or res.node is None:
        return res

    if res.node.current == head.current:
        res.result = head.current

    res.node = res.node.next

    return res


def lengthOfList(n: LinkedList):
    size = 0
    while n is not None:
        size += 1
        n = n.next

    return size
