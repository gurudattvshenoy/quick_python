class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def display(self):
        if self.head == None:
            return "List is empty..."
        temp = self.head
        print("Elements -> ",end='')
        while temp is not None:
            print("{}".format(temp.data),end=", ")
            temp = temp.next

linkedList = LinkedList()
linkedList.insert_at_end(4233)
linkedList.insert_at_front(10)
linkedList.insert_at_front(29)
linkedList.insert_at_end(2)
linkedList.insert_at_end(233)
linkedList.display()

