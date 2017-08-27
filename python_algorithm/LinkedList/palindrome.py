# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from LinkedList import LinkedList


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
