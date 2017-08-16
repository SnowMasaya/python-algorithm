# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from LinkedList import LinkedList


def print_list(node: LinkedList=None) -> None:
    while(node):
        print(node)
        node = node.next


def make_linked_list()-> LinkedList:
    linkedlist = LinkedList(current_node='first')
    linkedlist2 = LinkedList(current_node='second')
    linkedlist3 = LinkedList(current_node='third')
    linkedlist4 = LinkedList(current_node='first')

    linkedlist.next = linkedlist2
    linkedlist2.next = linkedlist3
    linkedlist3.next = linkedlist4
    return  linkedlist

def make_linked_list_number(number_list: list)-> LinkedList:
    linkedlist = None

    for number in number_list:
        if linkedlist is None:
            linkedlist = LinkedList(current_node=number)
        else:
            linkedlist.next = LinkedList(current_node=number)
            linkedlist = linkedlist.next

    return  linkedlist
