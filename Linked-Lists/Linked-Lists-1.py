# Starter code

class NodeType:
    def __init__(self,name,pointer):
        self.name = name
        self.pointer = pointer
    #end constructor
    def __repr__(self) -> str:      #repr = represent
      return f'(Name: {self.name}; Pointer: {self.pointer})'
    #end function
#end class
x = NodeType("Bob",-1)
x.name = "Ava"
x.pointer = 0
print(x.name, x.pointer)
myList = [NodeType("",x+1) for x in range(9)]
myList.append(NodeType("",-1))
for node in myList:
    print(node.pointer)

# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()


