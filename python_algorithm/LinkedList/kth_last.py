# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from LinkedList import LinkedList


def printKthToLast(head: LinkedList=None, k: int=0) -> int:
    if head is None:
        return 0
    index = printKthToLast(head.next, k) + 1
    if index == k:
        print("{0} th to last node is {1}".format(k, head.current))
    return index


class Index(object):

    def __init__(self):
        self.value = 0


def kthToLast(*args):
    if len(args) == 2:
        idx = Index()
        return kthToLast(args[0], args[1], idx)
    elif len(args) == 3:
        if args[0] == None:
            return None
        node = kthToLast(args[0].next, args[1], args[2])
        args[2].value = args[2].value + 1
        if args[2].value == args[1]:
            return args[0]
        return node


def nthToLast(head: LinkedList, k: int) -> LinkedList:
    p1 = head
    p2 = head

    for i in range(k):
        if p1 == None:
            return None
        p1 = p1.next

    while p1 != None:
        p1 = p1.next
        p2 = p2.next

    return p2
