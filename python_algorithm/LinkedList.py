# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from typing import Any


class LinkedList(object):

    def __init__(self, current_node: str=None,
                 next_node: Any=None)-> None:
        self.current = current_node
        self.next = next_node

    def __str__(self) -> str:
        return str(self.current)

def print_list(node: LinkedList=None) -> None:
    while(node):
        print(node)
        node = node.next

def deleteDups(node: LinkedList=None):
    set_data = []
    node_previous = None
    while(node):
        if node.current in set_data:
            node_previous.next = node.next
        else:
            set_data.append(node.current)
            node_previous = node
        node = node.next

if __name__ == "__main__":
    linkedlist = LinkedList(current_node='first')
    linkedlist2 = LinkedList(current_node='second')
    linkedlist3 = LinkedList(current_node='third')
    linkedlist4 = LinkedList(current_node='first')

    linkedlist.next = linkedlist2
    linkedlist2.next = linkedlist3
    linkedlist3.next = linkedlist4

    print_list(linkedlist)
    deleteDups(linkedlist)
    print('-----Delete Duplicate----')
    print_list(linkedlist)
