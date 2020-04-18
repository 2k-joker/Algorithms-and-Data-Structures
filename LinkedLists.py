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


