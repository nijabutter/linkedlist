from linkedlist import *

head = Node(1)
head.genList(10)
head.printList()

last = None
current = head
while current != None:
   n = current.next
   current.next = last
   last = current
   current = n

last.printList()

