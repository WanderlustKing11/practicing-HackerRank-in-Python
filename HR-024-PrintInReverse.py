# HackerRank - Data Structures
# Print in Reverse
# By Douglas Horville

# Given a pointer to the head of a singly-linked list, print each data 
# value from the reversed list. If the given list is empty, do not print anything.

# reversePrint has the following parameters:

# SinglyLinkedListNode pointer head: a reference to the head of the list

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

def reversePrint(llist):
    # Write your code here
    if llist is None:
        return None
    
    prev = None
    current = llist
    next = None

    while current != None:
        next = current.next   # Step 1: Store the next node
        current.next = prev   # Step 2: Reverse the current node's pointer
        prev = current        # Step 3: Move prev to current
        current = next        # Step 4: Move current to next

    return prev


###############################################################
###########  Main ###########

def main():
    inputFile = open('./test/024-out.txt', 'r')
    content = inputFile.read().split()
    inputFile.close()

    n = int(content[0])

    # Initialize the linked list
    llist = SinglyLinkedList()

    for line in content[1:]:
      list_item = int(line.rstrip())
      llist.insert_node(list_item)
    
    print("Original list:")
    print_singly_linked_list(llist.head, ' -> ')
    print('\n')

    llist.head = reversePrint(llist.head)

    print("Reversed list:")
    print_singly_linked_list(llist.head, ' -> ')
    print('\n')
    print('='*40)

main()