class Node:
    def __init__(self,element):
        self.element = element
        self.left = None
        self.right = None
#------creating the objects--------
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# '''
#         a
#         /\
#         b c
#         /\ \
#         d e f
# '''
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# #-----------iterative approach---
# #-------------depth first/ pre order  tree traversal implementation----------

# stack = [a]
# result = []

# while len(stack)>0:
#     current = stack.pop()
#     result.append(current.element)
#     if current.right:
#         stack.append(current.right)
#     if current.left:
#         stack.append(current.left)

# print('result = ',result)

#----recursive function---

def preorder_recursive(node,result):
    if node == None:
        return
    result.append(node.element)
    preorder_recursive(node.left,result)
    preorder_recursive(node.right,result)

def postorder_recursive(node, result):
    '''
        d -> e -> b -> f ->c -> a
    '''
    if node == None:
        return
    postorder_recursive(node.left,result)
    postorder_recursive(node.right,result)
    result.append(node.element)

def inorder_recurssive(node,result):
    '''
     d -> b -> e -> a -> c -> f
    '''
    if node == None:
        return 
    inorder_recurssive(node.left,result)
    result.append(node.element)
    inorder_recurssive(node.right,result)

from collections import deque
def level_order(node):   # breadth first traversal
    '''
         a
        / \ 
       b    c
      / \    \ 
     d   e    f

     output = a -> b -> c -> d -> e ->f
     # queue datastructure

     queue =      
     current =  f   
     
     result = [a,b,c,d,e,f]
    '''
    if node == None:
        return 
    queue = deque()
    queue.append(node)
    result = []

    while queue:
        current = queue.popleft()
        result.append(current.element)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result




a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
'''
        a
        /\
        b c
        /\ \
        d e f
'''
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f



result = []
preorder_recursive(a,result)
print('pre order result = ',result)


result1 = []
postorder_recursive(a,result1)
print('post order result = ',result1)


result2 = []
inorder_recurssive(a,result2)
print('inorder result = ',result2)

print('level order',level_order(a))
