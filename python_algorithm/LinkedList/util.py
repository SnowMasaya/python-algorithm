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
    return linkedlist

def make_linked_list_number(number_list: list)-> LinkedList:

    linked_list_array = []
    for i in range(len(number_list)):
        linked_list_array.append(LinkedList(current_node=number_list[i]))

    for i in range(len(number_list) - 1):
        linked_list_array[i].next = linked_list_array[i + 1]

    return linked_list_array[0]
