class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right =None

class Tree:
    def __init__(self):
        self.root = None   #root - корень

    def insert(self, value): #метод через который будем записывать в дерево
        def _insert(node: Node, value):
            if node is None:
                return Node(value)
            else:
                if value < node.value:
                    node.left = _insert(node.left, value)
                else:
                    node.right = _insert(node.right, value)
            return node
    
        self.root = _insert(self.root, value) #сохраняем в дерево коренной элемент


#отсортированные значения метод
    def order(self):
        def _order(node: Node):
            if node:
                _order(node.left)
                print(node.value, end= " | ")
                _order(node.right)
        _order(self.root)

t = Tree()
t.insert(100)
t.insert(55)
t.insert(240)
t.insert(17)
t.insert(34)

t.order()
        

        
