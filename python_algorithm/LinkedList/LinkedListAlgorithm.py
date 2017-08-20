# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from delete_duplicate import deleteDups, deleteDupsNonbuffer
from util import make_linked_list, print_list, make_linked_list_number
from kth_last import printKthToLast, kthToLast, nthToLast
from delete_node import deleteNode
from partition import partition


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
    print_list(linkedlist)
    linkedlist = linkedlist.next
    print('Delete process')
    linkedlist = deleteNode(linkedlist)
    print_list(linkedlist)

    print('-----Partition element Linked list ----')
    linkedlist = make_linked_list_number(number_list=[2, 5, 3, 1, 2])
    print_list(linkedlist)
    print('-----After Partition element Linked list ----')
    linkedlist = partition(linkedlist, 3)
    print_list(linkedlist)
