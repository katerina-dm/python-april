#это так всегда составляется
class Node:
    def __init__(self, data):
        self.data = data
        self.nex_link = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

#добавляем
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        else:
            old_head = self.head
            self.head = new_node
            self.head.nex_link = old_head


    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            last_elem = self.head 
            while last_elem.nex_link is not None: 
                last_elem = last_elem.nex_link
            last_elem.nex_link = new_node

    def display(self):
        if self.head is None:
           print("None") 
        else:
            current = self.head
            while current.nex_link is not None:
                print(current.data, end=" -> ")
                current =current.nex_link
            print(current.data, end=" -> ")
            print("None")

lst = SingleLinkedList()
lst.display()

lst.append(5)
lst.append(13)
lst.append("boat")

lst.display()

#добывили новый элемент
lst.append(2)
lst.display()

lst.push(0)
lst.display()

