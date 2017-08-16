# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from LinkedList import LinkedList


def deleteNode(n :LinkedList) -> LinkedList:
    if n == None or n.next == None:
        return False

    next = n.next
    n.current = next.current
    n.next = next.next
    return n
