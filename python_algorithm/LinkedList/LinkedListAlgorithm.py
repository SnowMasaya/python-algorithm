# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from LinkedList import LinkedList
from delete_duplicate import deleteDups, deleteDupsNonbuffer
from util import make_linked_list, print_list
from kth_last import printKthToLast, kthToLast, nthToLast
from delete_node import deleteNode


if __name__ == "__main__":

    linkedlist = make_linked_list()
    print_list(linkedlist)
    deleteDups(linkedlist)
    print('-----Delete Duplicate----')
    print_list(linkedlist)

    print('-----Retry----')
    linkedlist = make_linked_list()
    deleteDupsNonbuffer(linkedlist)
    print('-----Delete Duplicate Non buffer----')
    print_list(linkedlist)

    print('-----Linked list last node----')
    linkedlist = make_linked_list()
    printKthToLast(linkedlist, 2)
    print(kthToLast(linkedlist, 2))
    print(kthToLast(linkedlist, 3))
    print(nthToLast(linkedlist, 3))

    print('-----Delete element Linked list ----')
    linkedlist = make_linked_list()
    # deleteNode(linkedlist)
