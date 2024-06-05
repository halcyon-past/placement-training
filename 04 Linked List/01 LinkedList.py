class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def length(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" ")
            cur_node = cur_node.next
        print()

if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.prepend(0)
    llist.print_list()