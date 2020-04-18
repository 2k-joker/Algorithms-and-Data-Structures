## Insert a node at a position k in a linkedlist ##

def insertNodeAtPosition(head, data, position):
    newNode = Node(data)
    currentNode = head
    
    counter = 0
    while counter < (position - 1):
        if currentNode.next is None:
            currentNode.next = newNode
            return head
        currentNode = currentNode.next
        counter += 1

    newNode.next = currentNode.next
    currentNode.next = newNode                 

    return head


## Insert a new node into a sorted doublylinked list such that the list is still sorted afterwards ##
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev

def sortedInsert(head, data):
    newNode = DoublyLinkedListNode(data)
    currentNode = head

    if currentNode.data > newNode.data:
        newNode.next = currentNode
        currentNode.prev = newNode
        head = newNode
        return head

    
    while True:
        if currentNode.next is None:
            currentNode.next = newNode
            newNode.prev = currentNode
            break
        elif currentNode.next.data >= newNode.data:
            newNode.next = currentNode.next
            currentNode.next = newNode
            currentNode.next.prev = newNode
            newNode.prev = currentNode
            break
        currentNode = currentNode.next

    return head

## Reverse SinglyLinked list ##
# There's at least one node in the list
def reverseLinkedList(head):
  
    if head.next is None:
        return head
    currentPointer = head
    previousPointer = None

    while currentPointer:
        holder = currentPointer.next
        currentPointer.next = previousPointer
        previousPointer = currentPointer
        currentPointer = holder

    return previousPointer

## Reverse Doublylinked list ##
# There is at least one note in the list
def reverseLinkedList2(head):
    currentPointer = head
    previousPointer = None

    if currentPointer.next is None:
        return head

    while currentPointer:
        previousPointer = currentPointer.prev
        currentPointer.prev = currentPointer.next
        currentPointer.next = previousPointer
        currentPointer = currentPointer.prev
    
    return previousPointer.prev
