# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from LinkedList import LinkedList
import math


class Result(object):
    def __init__(self, tail: LinkedList, size: int):
        self.tail = tail
        self.size = size


def find_inter_section(list1: LinkedList, list2: LinkedList)-> LinkedList:
    if list1 is None or list2 is None:
        return None

    result1 = getTailAndSize(list1)
    result2 = getTailAndSize(list2)

    if result1.tail != result2.tail:
        return None

    if result1.size < result2.size:
        shorter = list1
        longer = list2
    else:
        shorter = list2
        longer = list1

    longer = getKthNode(longer, math.fabs(result1.size - result2.size))

    while shorter is not longer:
        shorter = shorter.next
        longer = longer.next

    return longer


def getTailAndSize(list: LinkedList) -> Result:
    if list is None:
        return None

    size = 1
    current = list
    while current.next is not None:
        size += 1
        current = current.next

    return Result(current, size)


def getKthNode(head: LinkedList, k: int):
    current = head
    while k>0 and current is not None:
        current = current.next
        k -= 1

    return current
