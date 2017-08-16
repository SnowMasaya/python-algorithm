# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from LinkedList import LinkedList

def partition(node: LinkedList, x: int) -> LinkedList:
    beforeStart = None
    beforeEnd = None
    afterStart = None
    afterEnd = None

    while node is not None:
        next = node.next
        if node.current < x :
            if beforeStart is None:
                beforeStart = node
                beforeEnd = beforeStart
            else:
                beforeEnd.next = node
                beforeEnd = node
        else:
            if afterStart is None:
                afterStart = node
                afterEnd = afterStart
            else:
                afterEnd.next = node
                afterEnd = node
        node = next

    if beforeStart is None:
        return afterStart

    beforeEnd.next = afterStart
    return beforeStart
