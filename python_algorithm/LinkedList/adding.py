# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from LinkedList import LinkedList

def addLists(l1: LinkedList, l2: LinkedList, carry: int) -> LinkedList:
    """
    Add two list
    For example
         7 -> 1 -> 6
       + 5 -> 9 -> 2
         2 -> 1 -> 9
    :param l1: 
    :param l2: 
    :param carry: 
    :return: 
    """
    if l1 is None and l2 is None and carry == 0:
        return None

    result = LinkedList()

    value = carry

    if l1 is not None:
        value += l1.current

    if l2 is not None:
        value += l2.current

    result.current = value % 10

    if l1 is not None or l2 is not None:
        more = addLists(None if l1 is None else l1.next,
                        None if l2 is None else l2.next,
                        1 if value >= 10 else 0)
        result.next = more

    return result

class PartialSum(object):

    def __init__(self):
        self.sum = None
        self.carry = 0


def addlistsSecond(l1: LinkedList, l2: LinkedList) -> LinkedList:
    len1 = len(l1)
    len2 = len(l2)

    if len1 < len2:
        l1 = paddList(l1, len2 - len1)
    else:
        l2 = paddList(l2, len1 - len2)

    sum = addListsHelper(l1, l2)

    if sum.curry == 0:
        return sum.sum
    else:
        result = insertBefore(sum.sum, sum.curry)
        return result


def addListsHelper(l1: LinkedList, l2: LinkedList) -> PartialSum:
    if l1 is None and l2 is None:
        sum = PartialSum()
        return sum

    sum = addListsHelper(l1.next, l2.next)

    val = sum.curry + l1.current + l2.current

    full_result = insertBefore(sum.sum, val % 10)

    sum.sum = full_result
    sum.carry = val / 10
    return sum


def paddList(l: LinkedList, padding: int) -> LinkedList:
    head = l
    for i in range(padding):
        head = insertBefore(head, 0)

    return head


def insertBefore(list: LinkedList, data: int) -> LinkedList:
    node = LinkedList()
    node.current = data
    if list is not None:
        node.next = list
    return node




