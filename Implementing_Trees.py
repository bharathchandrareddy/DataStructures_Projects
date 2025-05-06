'''
Trees are the foundational concepts for other advanced algorithms and data structures.
so, learning everything about trees helps to understand other concepts easily. It's also one 
of the most widly used data structure in real time. Its a data structure that represents the heirarchical relationship(non-linear) between nodes.
Applications:
1. Searching and sorting elements
2. Routing networks
3. Machine learning (Decision Tree)
4. To implement tries, heap/priority queue, Back tracking
'''


class Tree:
    def __init__(self, node, ):
        
        pass

    class Position:
        def element(self):
            '''
            return the element stored at position p
            '''
            raise NotImplementedError('Must be implemented by subclass; in out case it is linked binary tree')
        def __eq__(self, value):
            '''
            return true if other position represents the same
            '''
            raise NotImplementedError('must be implemented in subclass')
        def __ne__(self, value):
            '''
            return true if other does not represent the same location. i.e: opposite to __eq__()
            '''
            
            return not (self==value)
    def root(self,p):
        '''
        return position representing the tree's root
        '''
        raise NotImplementedError('must be implemented by subclass')
    def is_root(self,p):
        '''return true if the position p is root of the tree'''
        return self.root() == p
    def parent(self,p):
        '''
        return position representing parent of p, none if p is the root
        '''
        raise NotImplementedError('must be implemented by subclass')
    
    def num_children(self,p):
        '''return the no of childer for given position p, none if p is leaf'''
        raise NotImplementedError('must be implemented by subclass')
    
    def children(self,p):
        '''generate an iteration of positions representing p's childern'''
        raise NotImplementedError('must be implemented in subclass')
    
    def __len__(self):
        '''return the total number of elements in the tree'''
        raise NotImplementedError('Must be implemented in subclass')
    
    def is_root(self,p):
        '''
        return true if position p is the root
        '''
        return self.root() == p

    def is_leaf(self,p):
        '''
        return true if position p is the leaf
        '''
        return self.num_children()==p
    
    def is_empty(self,p):
        '''
        return true if the tree is empty
        '''
        return len(self) == 0
    

class BinaryTree(Tree):
    '''
     Abstract parent class representing a tree with simple regular methhods
    '''
    #----------additional parameters for the binary tree-----------
    
    def left(self,p):
        '''
        return a position representing p's left child
        none if p dosen't have a left child
        '''
        raise NotImplementedError('must be implemented in subclass')
    def right(self,p):
        '''
        return a postion representing p's right child.
        none if p does not have a right child
        '''
        raise NotImplementedError('must be implemented by subclass')
    def sibling(self,p):
        '''
        return a position representing p's sibling or none if no sibling
        '''
        parent = self.parent(p)
        if parent is None:  #whhich means Root node
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)   # posibbly none
            else:
                return self.left(parent)  # posibbly none
    def children(self, p):
        '''
        generatingg an iteration of chhilder of position p
        '''
        if self.left(p) is not None:
            yield self.left(p)

        if self.right(p) is not None:
            yield self.right(p)

class Linked_Binary_Tree(BinaryTree):
    '''
    linked representation of a binary tree
    '''
    class Node:   #non public class for storing a node
        
        def __init__(self,element,parent=None,left=None,right=None):
            self._element = element
            self._parent = parent
            self._left=left
            self._right = right
    class Position:
        '''
        an abstraction representing the location of single element.
        This class is an abstraction of node class to provide controlled way to access and interact with nodes
        '''
        def __init__(self,container,node):
            '''
            constructor should not be invoked by user
            '''
            self._container = container   #_container is used as naming convention stating that this variable is only used for internel purposes and not to expose it other methods
            self._node = node
        def element(self):
            '''
            return the element stored at this positon
        
            '''
            return self._node._element
        
        def __eq__(self,other):
            '''
            return true if other is a position representing the same location
            '''
            return type(other) is type(self) and other._node is self._node
        
    def _validate(self,p):
        '''return associated node if position is valid
        '''
        if not isinstance(p,self.Position):
            raise TypeError('p must be proper position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node
    def _make_position(self,node):
        '''
        return position instance for given node (none if no node)

        '''
        return self.Position(self,node) if node is not None else None
    
    #----------binary tree constructor----------

    def __init__(self):
        '''
        creating empty binary tree
        '''
        self._root = None
        self._size = 0
    
    #-----------public accessories--
    def __len__(self):
        '''
        return the total number if elements in the tree
        '''
        return self._size
    
    def root(self):
        '''
        reutn the root element
        '''
        return self._make_position(self._root)
    
    def parent(self, p):
        '''return the position of parent, None is p is root'''
        node = self._validate(p)
        return self._make_position(node._parent)
    