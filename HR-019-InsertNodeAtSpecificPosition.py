# HackerRank - Data Structures
# Insert a node at a specific position in a linked list
# By Douglas Horville

# Given the pointer to the head node of a linked list and an integer to 
# insert at a certain position, create a new node with the given integer 
# as its data attribute, insert this node at the desired position and return the head node.

# A position of 0 indicates head, a position of 1 indicates one node away 
# from the head and so on. The head pointer given may be null meaning that the initial list is empty.

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

def print_singly_linked_list(node, sep, fptr):
    first = True
    while node:
        if first:
            first = False
        else:
            if fptr:
                fptr.write(sep)
            else:
                print(sep, end='')

        if fptr:
            fptr.write(str(node.data))
        else:
            print(node.data, end='')

        node = node.next

    if not fptr:
        print()

##################################################################################
########## My Function ##########

def insertNodeAtPosition(llist, data, position):
    # Write your code here
    new_node = SinglyLinkedListNode(data)

    if position == 0:
        new_node.next = llist
        llist = new_node
        return llist

    current = llist
    while (position) > 1:
        current = current.next
        position -= 1
    new_node.next = current.next
    current.next = new_node
    return llist
    

def main():
    ############################################################
    ######## Sample Test Case 1 ########
    testList1 = SinglyLinkedList()
    testList1.insert_node(16)
    testList1.insert_node(13)
    testList1.insert_node(7)
    # print_singly_linked_list(testList1.head, ' -> ', None)  # Print the test Linked List
    print("\nInsterting 1 at position 2:")
    testList1.head = insertNodeAtPosition(testList1.head, 1, 2)
    print_singly_linked_list(testList1.head, ' -> ', None)
    ############################################################
    ######## Sample Test Case 2 ########
    testList2 = SinglyLinkedList()
    testList2.insert_node(11)
    testList2.insert_node(9)
    testList2.insert_node(19)
    testList2.insert_node(10)
    testList2.insert_node(14)
    print("\nInserting 20 at position 3:")
    testList2.head = insertNodeAtPosition(testList2.head, 20, 3)
    print_singly_linked_list(testList2.head, ' -> ', None)
################################################################
    ######## Sample Test Case 3 ########
    testList3 = SinglyLinkedList()
    testList3.insert_node(1)
    testList3.insert_node(2)
    testList3.insert_node(3)
    testList3.insert_node(4)
    testList3.insert_node(5)
    testList3.insert_node(6)
    print("\nInserting 7 at position 5:")
    testList3.head = insertNodeAtPosition(testList3.head, 7, 5)
    print_singly_linked_list(testList3.head, ' -> ', None)


main()