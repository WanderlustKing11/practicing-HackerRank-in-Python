# HackerRank - Data Structures
# Linked Lists
# By Douglas Horville

# This is an exercise to practice traversing a linked list. 
# Given a pointer to the head node of a linked list, print each node's `data` element, 
# one per line. If the head pointer is null (indicating the list is empty), 
# there is nothing to print.

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



####################################################################################

def printedLinkedList(head):
  if head == None:
      return None
  
  current = head
  while current != None:
    print(current.data)
    current = current.next


def main():
  linked_list = SinglyLinkedList()
  data = [3,45,7,68,91,42]
  for item in data:
     linked_list.insert_node(item)
  printedLinkedList(linked_list.head)

main()