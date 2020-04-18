## Insert a node at a position k in a linkedlist ##

def insertNodeAtPosition(head, data, position):
    newNode = SinglyLinkedListNode(data)
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
