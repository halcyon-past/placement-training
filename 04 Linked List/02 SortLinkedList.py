class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def sortList(self):
        if self.head is None:
            return
        current = self.head
        while current:
            next = current.next
            while next:
                if current.data > next.data:
                    current.data, next.data = next.data, current.data
                next = next.next
            current = current.next
        
if __name__=="__main__":
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)
    llist.printList()
    llist.sortList()
    llist.printList()

