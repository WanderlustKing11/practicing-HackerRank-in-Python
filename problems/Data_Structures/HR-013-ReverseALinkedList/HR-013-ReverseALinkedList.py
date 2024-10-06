# HackerRank - Data Structures
# Reverse a Linked List
# By Douglas Horville

# Given the pointer to the head node of a linked list, change the next pointers of 
# the nodes so that their order is reversed. The head pointer given may be null 
# meaning that the initial list is empty.

# reversePrint has the following parameters:
# SinglyLinkedListNode pointer head: a reference to the head of a list

# Returns:
# SinglyLinkedListNode pointer: a reference to the head of the reversed list

###############################################################
###########  Classes  ###########

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')


###############################################################
###########  Solve  ###########
import os

def reverse(llist):
    if llist is None:
        return None
    
    prev = None
    current = llist

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev



###############################################################
###########  Main ###########

def main():
  script_dir = os.path.dirname(os.path.abspath(__file__))
  input_file_path = os.path.join(script_dir, 'test', 'DS-013-input.txt')

  with open(input_file_path, 'r') as inputFile:
    content = inputFile.read().strip()
    lines = content.splitlines()

    # First line contains the number of test cases
    t = int(lines[0])
    index = 1  # Start from the second line
    for _ in range(t):
      # Get the number of elements in the linked list for this test case
      n = int(lines[index])
      index += 1

      # Initialize the linked list
      llist = SinglyLinkedList()
      # Read the next 'n' lines as linked list elements
      for i in range(n):
        list_item = int(lines[index].strip())
        llist.insert_node(list_item)
        index += 1
      
      print("Original list:")
      print_singly_linked_list(llist.head, ' -> ')
      print('')

      reversed_list_head = reverse(llist.head)

      print("Reversed list:")
      print_singly_linked_list(reversed_list_head, ' -> ')
      print()
      print('='*40)

if __name__ == '__main__':
  main()