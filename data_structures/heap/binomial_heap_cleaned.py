

"""
Binomial Heap
Reference: Advanced Data Structures, Peter Brass
"""


class Node:
    

    def __init__(self, val):
        self.val = val
        
        self.left_tree_size = 0
        self.left = None
        self.right = None
        self.parent = None

    def mergeTrees(self, other):
        
        assert self.left_tree_size == other.left_tree_size, "Unequal Sizes of Blocks"

        if self.val < other.val:
            other.left = self.right
            other.parent = None
            if self.right:
                self.right.parent = other
            self.right = other
            self.left_tree_size = self.left_tree_size * 2 + 1
            return self
        else:
            self.left = other.right
            self.parent = None
            if other.right:
                other.right.parent = self
            other.right = self
            other.left_tree_size = other.left_tree_size * 2 + 1
            return other


class BinomialHeap:
    

    def __init__(self, bottom_root=None, min_node=None, heap_size=0):
        self.size = heap_size
        self.bottom_root = bottom_root
        self.min_node = min_node

    def mergeHeaps(self, other):
        

        
        if other.size == 0:
            return
        if self.size == 0:
            self.size = other.size
            self.bottom_root = other.bottom_root
            self.min_node = other.min_node
            return
        
        self.size = self.size + other.size

        
        if self.min_node.val > other.min_node.val:
            self.min_node = other.min_node
        

        
        combined_roots_list = []
        i, j = self.bottom_root, other.bottom_root
        while i or j:
            if i and ((not j) or i.left_tree_size < j.left_tree_size):
                combined_roots_list.append((i, True))
                i = i.parent
            else:
                combined_roots_list.append((j, False))
                j = j.parent
        
        for i in range(len(combined_roots_list) - 1):
            if combined_roots_list[i][1] != combined_roots_list[i + 1][1]:
                combined_roots_list[i][0].parent = combined_roots_list[i + 1][0]
                combined_roots_list[i + 1][0].left = combined_roots_list[i][0]
        
        i = combined_roots_list[0][0]
        while i.parent:
            if (
                (i.left_tree_size == i.parent.left_tree_size) and (not i.parent.parent)
            ) or (
                i.left_tree_size == i.parent.left_tree_size
                and i.left_tree_size != i.parent.parent.left_tree_size
            ):

                
                previous_node = i.left
                next_node = i.parent.parent

                
                i = i.mergeTrees(i.parent)

                
                i.left = previous_node
                i.parent = next_node
                if previous_node:
                    previous_node.parent = i
                if next_node:
                    next_node.left = i
            else:
                i = i.parent
        
        while i.left:
            i = i.left
        self.bottom_root = i

        
        other.size = self.size
        other.bottom_root = self.bottom_root
        other.min_node = self.min_node

        
        return self

    def insert(self, val):
        
        if self.size == 0:
            self.bottom_root = Node(val)
            self.size = 1
            self.min_node = self.bottom_root
        else:
            
            new_node = Node(val)

            
            self.size += 1

            
            if val < self.min_node.val:
                self.min_node = new_node
            
            self.bottom_root.left = new_node
            new_node.parent = self.bottom_root
            self.bottom_root = new_node

            
            while (
                self.bottom_root.parent
                and self.bottom_root.left_tree_size
                == self.bottom_root.parent.left_tree_size
            ):

                
                next_node = self.bottom_root.parent.parent

                
                self.bottom_root = self.bottom_root.mergeTrees(self.bottom_root.parent)

                
                self.bottom_root.parent = next_node
                self.bottom_root.left = None
                if next_node:
                    next_node.left = self.bottom_root

    def peek(self):
        
        return self.min_node.val

    def isEmpty(self):
        return self.size == 0

    def deleteMin(self):
        
        

        
        min_value = self.min_node.val

        
        if self.size == 1:
            
            self.size = 0

            
            self.bottom_root = None

            
            self.min_node = None

            return min_value
        
        
        
        if self.min_node.right is None:
            
            self.size -= 1

            
            self.bottom_root = self.bottom_root.parent
            self.bottom_root.left = None

            
            self.min_node = self.bottom_root
            i = self.bottom_root.parent
            while i:
                if i.val < self.min_node.val:
                    self.min_node = i
                i = i.parent
            return min_value
        
        
        bottom_of_new = self.min_node.right
        bottom_of_new.parent = None
        min_of_new = bottom_of_new
        size_of_new = 1

        
        while bottom_of_new.left:
            size_of_new = size_of_new * 2 + 1
            bottom_of_new = bottom_of_new.left
            if bottom_of_new.val < min_of_new.val:
                min_of_new = bottom_of_new
        
        if (not self.min_node.left) and (not self.min_node.parent):
            self.size = size_of_new
            self.bottom_root = bottom_of_new
            self.min_node = min_of_new
            
            return min_value
        
        
        newHeap = BinomialHeap(
            bottom_root=bottom_of_new, min_node=min_of_new, heap_size=size_of_new
        )

        
        self.size = self.size - 1 - size_of_new

        
        previous_node = self.min_node.left
        next_node = self.min_node.parent

        
        self.min_node = previous_node or next_node
        self.bottom_root = next_node

        
        
        if previous_node:
            previous_node.parent = next_node

            
            self.bottom_root = previous_node
            self.min_node = previous_node
            while self.bottom_root.left:
                self.bottom_root = self.bottom_root.left
                if self.bottom_root.val < self.min_node.val:
                    self.min_node = self.bottom_root
        if next_node:
            next_node.left = previous_node

            
            i = next_node
            while i:
                if i.val < self.min_node.val:
                    self.min_node = i
                i = i.parent
        
        self.mergeHeaps(newHeap)

        return min_value

    def preOrder(self):
        
        
        top_root = self.bottom_root
        while top_root.parent:
            top_root = top_root.parent
        
        heap_preOrder = []
        self.__traversal(top_root, heap_preOrder)
        return heap_preOrder

    def __traversal(self, curr_node, preorder, level=0):
        
        if curr_node:
            preorder.append((curr_node.val, level))
            self.__traversal(curr_node.left, preorder, level + 1)
            self.__traversal(curr_node.right, preorder, level + 1)
        else:
            preorder.append(("#", level))

    def __str__(self):
        
        if self.isEmpty():
            return ""
        preorder_heap = self.preOrder()

        return "\n".join(("-" * level + str(value)) for value, level in preorder_heap)



if __name__ == "__main__":
    import doctest

    doctest.testmod()
