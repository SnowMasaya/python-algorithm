# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from delete_duplicate import deleteDups, deleteDupsNonbuffer
from util import make_linked_list, print_list, make_linked_list_number
from kth_last import printKthToLast, kthToLast, nthToLast
from delete_node import deleteNode
from partition import partition, partion_short_code
from adding import addLists, addlistsSecond
from palindrome import is_palindrome, isPalinedromeSecond
from find_intersection import find_inter_section


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
    print('-----After2 Partition element Linked list ----')
    linkedlist = partion_short_code(linkedlist, 3)
    print_list(linkedlist)

    print('-----adding element Linked list ----')
    linkedlist = make_linked_list_number(number_list=[7, 1, 6])
    print_list(linkedlist)
    print('-----adding element Linked list2 ----')
    linkedlist2 = make_linked_list_number(number_list=[5, 9, 2])
    print_list(linkedlist)
    print('-----adding process ----')
    resultlist = addLists(linkedlist, linkedlist2, 0)
    print_list(resultlist)

    print('-----adding second element Linked list ----')
    linkedlist = make_linked_list_number(number_list=[1, 2, 3, 4])
    print_list(linkedlist)
    print('-----adding element Linked list2 ----')
    linkedlist2 = make_linked_list_number(number_list=[5, 6, 7])
    print_list(linkedlist2)
    print('-----adding process ----')
    resultlist = addlistsSecond(linkedlist, linkedlist2)
    print_list(resultlist)

    print('-----Palindrome Linked list ----')
    linkedlist = make_linked_list_number(number_list=[0, 1, 2, 1, 0])
    print('-----Check palindrome Linked list ----')
    linkedlist2 = is_palindrome(linkedlist)
    print(linkedlist2)
    linkedlist = make_linked_list_number(number_list=[0, 1, 2, 1, 1])
    print('-----Check palindrome Linked list2 ----')
    linkedlist2 = is_palindrome(linkedlist)
    print(linkedlist2)

    print('-----Palindrome Linked list by the stack ----')
    print('-----Check palindrome Linked list ----')
    linkedlist = make_linked_list_number(number_list=[0, 1, 2, 1, 0])
    linkedlist2 = is_palindrome(linkedlist)
    print(linkedlist2)
    print('-----Check palindrome Linked list ----')
    linkedlist = make_linked_list_number(number_list=[0, 1, 2, 1, 1])
    linkedlist2 = is_palindrome(linkedlist)
    print(linkedlist2)

    print('-----Check palindrome recurse Linked list ----')
    linkedlist = make_linked_list_number(number_list=[0, 1, 2, 1, 0])
    result = isPalinedromeSecond(linkedlist)
    print(result)
    linkedlist = make_linked_list_number(number_list=[0, 1, 2, 1, 1])
    result = isPalinedromeSecond(linkedlist)
    print(result)
    linkedlist = make_linked_list_number(number_list=[0, 1, 2, 2, 2])
    result = isPalinedromeSecond(linkedlist)
    print(result)

    print('-----Check match Linked list ----')
    linkedlist = make_linked_list_number(number_list=[3, 1, 5, 9, 7, 2, 1])
    linkedlist2 = make_linked_list_number(number_list=[4, 6, 7, 2, 1])
    result = find_inter_section(linkedlist, linkedlist2)
    print(result)
