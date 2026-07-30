# Linked list consists of head and tail, tail is O(1)
# Changing the tail would require iterating from head to the very end , this is O(n)
# Adding item to the head O(1) 
# Removing item to the head O(1) 
#Adding in between head and tail is O(n) as it would require iterating from head to the very end
#Removing in between head and tail is O(n) as it would require iterating from head to the very end
# Lookup in the linkedin list would require iterating starting from head until its found so this is O(n)
#Linked List [ Append = O(1), Pop = O(n), Prepend = O(n), Pop First = O(1), Insert = O(n), Remove = O(n),
#Lookup by Index = O(n), Lookup by Value = O(n).

#Example of what LinkedList would look like 

head: {
  "value":11,
  "next":{
            "value": 3,
            "next":{
                      "value": 23,
                      "next":{
                                "value":7,
                                "next":None} #Tail
            }
  }

  #Printing Linked List:
  print(my_linked_list.head.next.next.value)

  #Creating a linked List Constructor with nodes

  class Node:
    def __init__(self, value):
      self.value = value
      self.next = None

  Class LinkedList:
    def __init__(self, value):
      new_node = Node(value)
      self.head = new_node
      self.tail = new_node
      self.length = 1
#performing tets 
# my_linked_list = LinkedList(4)
# print(my_linked_list.head.value)

#Printing the Linked-List

def print_list(self):
  temp = self.head
  while temp is not None:  #iterates oves the linkedlist until it reaches the end which = None
    print(temp.value)
    temp = text.next

