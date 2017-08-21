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

