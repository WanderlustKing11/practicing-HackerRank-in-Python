# HackerRank - Data Structures
# Delete a Node
# By Douglas Horville

# Delete the node at a given position in a linked list and return 
# a reference to the head node. The head is at position 0. 
# The list may be empty after you delete the node. In that case, return a null value.

# deleteNode has the following parameters:
# - SinglyLinkedListNode pointer llist: a reference to the head node in the list
# - int position: the position of the node to remove

# Returns
# - SinglyLinkedListNode pointer: a reference to the head of the modified list

# Input Format

# The first line of input contains an integer , the number of elements in the linked list.
# Each of the next  lines contains an integer, the node data values in order.
# The last line contains an integer, , the position of the node to delete.

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

# Define print to conosle if fptr is None
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
        print()  # To move to the next line after printing the list


###############################################################
###########  Solve  ###########


def deleteNode(llist, position):
  if llist == None:
      return None
  
  if position == 0:
      current  = llist
      llist = current.next
      return llist
  
  current = llist
  while position > 1:
      current = current.next
      position -= 1
  previous = current
  current = current.next
  if current.next == None:
      previous = previous.tail
      # previous.next = None
      # or maybe... previous.next = None ?
  else:
      previous.next = current.next
  return llist


###############################################################
###########  Main ###########

def main():
  inputFile = open('./test/023-out.txt', 'r')
  content = inputFile.read().split('---')
  inputFile.close()

  for test_case in content:
    lines = test_case.strip().split('\n')

    # Read the number of elements in the linked list
    llist_count = int(lines[0].rstrip())

    # Initialize the linked list
    llist = SinglyLinkedList()

    # Read node data values and insert into linked list
    for i in range(1, llist_count + 1):
      llist_item = int(lines[i].rstrip())
      llist.insert_node(llist_item)

    # Read the position of the node to delete
    position = int(lines[llist_count + 1].rstrip())
    
    # Print the original list
    print("Original list:")
    print_singly_linked_list(llist.head, ' -> ', fptr=None)
    print('\n')

    # Call deleteNode and print the modified list
    llist.head = deleteNode(llist.head, position)

    print("Modified list:")
    print_singly_linked_list(llist.head, ' -> ', fptr=None)
    print('\n')
    print('='*40)


main()
