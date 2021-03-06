# Linked list

Super simple linked list header and import for C and Python to quickly generate new linked lists and be able to print them

##### Usage

Python
```py
head = Node(1) # create a new linked list node
head.genList(10) # generate 10 children in ascending order
head.printList()
: 1->2->3->4->5->6->7->8->9->10
```

C
```c
Node* head = NewNode(1);
genList(head, 10);
printList(head);
: 1->2->3->4->5->6->7->8->9->10
```

###### Example

Reverse a linked list

```py
from linkedlist import *

head = Node(1)
head.genList(10)
head.printList(10)

last = None
current = head
while current != None:
    n = current.next
    current.next = last
    last = current
    current = n
last.printList()
```
