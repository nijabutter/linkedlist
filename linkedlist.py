import random
class Node:
    def __init__(self, value=0):
        self.next = None
        self.value = value
    def printList(self):
        head = self
        while head != None:
            print(head.value,end="")
            if head.next != None:
                print("->", end="")
            head = head.next
        print()
    def genList(self, count, mode="a", randomRange=(0,0)):
        if mode == "a":
            # ascending
            current = self
            for i in range(self.value+1, self.value+count):
                current.next = Node(i)
                current = current.next
        elif mode == "d":
            # descending:
            current = self
            for i in range(self.value-1, self.value-count, -1):
                current.next = Node(i)
                current = current.next 
        elif mode == "r":
            # random
            current = self
            for i in range(count):
                current.next = Node(random.randint(randomRange[0], randomRange[1]))
                current = current.next



