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

## Design a function to find a loop in a linked list ##
def findLoop(head):
    
    if head is None:
        return None

    slowRunner = fastRunner = head

    while  fastRunner is not None and fastRunner.next is not None :
        
        fastRunner = fastRunner.next.next
        slowRunner = slowRunner.next

        if fastRunner == slowRunner :
            break

    if fastRunner is None or fastRunner.next is None:
        return None

    slowRunner = head

    while slowRunner != fastRunner:
        slowRunner = slowRunner.next
        fastRunner = fastRunner.next

    return fastRunner

## Find the Intersection between two linked lists ##
# Lists are gauranteed to have an intersection
def findMergeNode(head1, head2):
    node1 = head1
    node2 = head2
    count1 = count2 = 0

    while node1:
        count1 += 1
        node1 = node1.next
    
    while node2:
        count2 += 1
        node2 = node2.next
    
    node1 = head1
    node2 = head2
    
    if count1 > count2:
        d = count1 - count2
        i =0
        while i < d:
            node1 = node1.next
            i += 1
        while node1 and node2:
            if node1 == node2:
                return node1.data
            node1 = node1.next
            node2 = node2.next
    elif count2 > count1:
        d = count2 - count1
        i =0
        while i < d:
            node2 = node2.next
            i += 1
        while node1 and node2:
            if node1 == node2:
                return node1.data
            node1 = node1.next
            node2 = node2.next
    else:
        while node1 and node2:
            if node1 == node2:
                return node1.data
            node1 = node1.next
            node2 = node2.next
        
    return None
