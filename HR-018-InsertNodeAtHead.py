# HackerRank - Data Structures
# Insert a node at the head of a linked list
# By Douglas Horville

# Given a pointer to the head of a linked list, insert a new node before the head. 
# The next value in the new node should point to head and the data value should be replaced 
# with a given value. Return a reference to the new head of the list. The head pointer 
# given may be null meaning that the initial list is empty.

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next


def insertNodeAtHead(llist, data):
    if llist is None:
        llist = SinglyLinkedListNode(data)
        return llist
    else:
        new_node = SinglyLinkedListNode(data)
        new_node.next = llist
        llist = new_node
        return llist

################################################################################

# if __name__ == '__main__':
#     fptr = open('./out.txt', 'w')

#     llist_count = int(input())

#     llist = SinglyLinkedList()

#     for _ in range(llist_count):
#         llist_item = int(input())
#         llist_head = insertNodeAtHead(llist.head, llist_item)
#         llist.head = llist_head
    
#     print_singly_linked_list(llist.head, '\n', fptr)
#     fptr.write('\n')
    
#     fptr.close()