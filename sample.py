# class Node:
#     def __init__(self,data):
#         self.value = data
#         self.next = None

    
# class Linked_list:
#     def __init__(self):
#         self.head = None

#     def append(self,value):
#         newNode = Node(value)
        
#         if self.head == None:
#             self.head = newNode 
#         else:
#             current_Node =  self.head

#             while current_Node.next is not None:

#                 current_Node = current_Node.next
#             current_Node.next = newNode



# ll = Linked_list()

# ll.append(10)
# ll.append(20)

# print(ll.head.next.value)

# class Node:
#     def __init__(self,data):
#         self.value = data
#         self.next = None

# class Linked_list:
#     def __init__(self):
#         self.head = None
#         self.length = 0
    
#     def append(self,value):
#         New_node = Node(value)
#         if self.head == None:
#             self.head = New_node
#         else:
#             Current_node = self.head

#             while Current_node.next is not None:
#                 Current_node = Current_node.next

#             Current_node.next = New_node
#         self.length += 1
#     def prepend(self,value):
#         New_node = Node(value) 
#         if self.head == None:
#             self.head = New_node
#         else:
#             New_node.next = self.head
#             self.head = New_node
#         self.length += 1
    
#     def __str__(self):
#         if self.head is None:
#             return "Linked List is empty"
#         else:
#             nodes=[]
#             current_Node = self.head
#             while current_Node is not None:
#                 nodes.append(str(current_Node.value))
#                 current_Node = current_Node.next
#             return ' -> '.join(nodes) + ' -> None'
#     def __len__(self):
#         return self.length
    


            

# ll = Linked_list()

# ll.append(10)
# ll.append(190)
# ll.prepend(100)


# print(ll.head.value)
# print("hee:",ll)



# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
    
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.length = 0
#     def append(self,data):
#         new_node = Node(data)

#         if self.head == None:
#             self.head = new_node
#         else:
#             current_node = self.head

#             while current_node.next is not None:
#                 current_node = current_node.next
#             current_node.next = new_node
#         self.length += 1
    
#     def prepend(self,data):
#         new_node = Node(data)
#         if self.head == None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
        
#     def __iter__(self):
#         current_node = self.head
#         while current_node is not None:
#             yield current_node.data
#             current_node=current_node.next


# ll = Linkedlist()

# ll.append(100)
# ll.prepend(101)
# for i in ll:
#     # print(ll.head.data)
#     print(i)






























    

        