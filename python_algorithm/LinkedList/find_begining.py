# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from LinkedList import LinkedList


def find_begining(head: LinkedList) -> LinkedList:
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if fast is None or fast.next is None:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast
