# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from LinkedList import LinkedList


def deleteDups(node: LinkedList=None) -> LinkedList:
    set_data = []
    node_previous = None
    while(node):
        if node.current in set_data:
            node_previous.next = node.next
        else:
            set_data.append(node.current)
            node_previous = node
        node = node.next

def deleteDupsNonbuffer(node: LinkedList=None) -> LinkedList:
    while(node):
        runner = node
        while(runner.next):
            if runner.next.current == node.current:
                runner.next = runner.next.next
            else:
                runner = runner.next
        node = node.next
