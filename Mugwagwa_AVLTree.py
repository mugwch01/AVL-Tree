#My name is Charles Mugwagwa. This is an implementation of an AVLTree.

import random

class AVLTree:    
    class AVLNode:
        def __init__(self,item,balance=0,left=None,right=None):
            self.item = item
            self.left = left
            self.right = right
            self.balance = balance
            self.height = AVLTree.Max(self.left,self.right)+1        
            
        def __iter__(self):        
            if self.left != None:
                for elem in self.left:
                    yield elem                        
            yield self.item
            
            if self.right != None:
                for elem in self.right:
                    yield elem    
             
        def check(node):#returns True if balanced. Otherwise, return False        
            #check node,check left,check right          
            okay_balances = [-1,0,1]           
            if node == None:
                return True
            if not node.getBalance() in okay_balances:                
                return False
            if not node.getLeft()==None:
                if not node.getLeft().check():                    
                    return False
            if not node.getRight()==None:
                if not node.getRight().check():                    
                    return False
            return True   
            
        def recalculate_balance(self):
            self.balance = AVLTree.balance(self)
            
        def recalculate_height(self):
            self.height = AVLTree.Max(self.left,self.right)+1
            
        def getVal(self):
            return self.item
            
        def getLeft(self):
            return self.left
        
        def getRight(self):
            return self.right
        
        def setLeft(self,item):
            self.left = item
            
        def setRight(self,item):
            self.right = item    
            
        def getBalance(self):
            return self.balance
            
        def getHeight(node):
            if node == None:
                return 0
            else:
                return node.height          
       
        def __repr__(self):           
            return "AVLTree.Node(" + repr(self.item) + ",balance=" + repr(self.balance) + ",left=" + repr(self.left) + ",right="+ repr(self.right) + ")"        
        
    def Max(left_node,right_node):
        #compares the height of the two nodes and returns the greater height
        if left_node == None:
            height_lst = 0
        else:
            height_lst = left_node.getHeight()
        if right_node == None:
            height_rst = 0
        else:
            height_rst = right_node.getHeight()
            
        if height_lst > height_rst:
            return height_lst
        else:
            return height_rst       
        
    def balance(node):#helper for recalculate_balance()
        if node.getLeft() == None:
            left_height = 0
        else:
            left_height = node.getLeft().getHeight()
        if node.getRight() == None:
            right_height = 0
        else:
            right_height = node.getRight().getHeight()            
        return right_height - left_height        
    
    def __init__(self,root=None):
        self.root = root        
                    
    def __iter__(self): #yield tree values in ascending order      
        return self.root.__iter__()
        
    def rotateRight(root):        
        x = root.getLeft()
        root.setLeft(None)        
        
        if x.getRight()==None:
            x.setRight(root)
            root.recalculate_height()
            root.recalculate_balance()            
            x.recalculate_height()
            x.recalculate_balance()              
            return x
            
        elif x.getLeft() == None:  
            new_root = x.getRight()
            new_root.setRight(root)
            x.setRight(None)            
            new_root.setLeft(x)             
            x.recalculate_height()
            x.recalculate_balance()
            root.recalculate_height()
            root.recalculate_balance()  
            new_root.recalculate_height()
            new_root.recalculate_balance()            
            return new_root
        
        else:#root has left and right child
            root.setLeft(x.getRight())
            x.setRight(root)
            root.getLeft().recalculate_height()
            root.getLeft().recalculate_balance()
            root.recalculate_height()
            root.recalculate_balance()
            x.recalculate_height()
            x.recalculate_balance()            
            return x             
        
    def rotateLeft(root):  
        x = root.getRight() 
        root.setRight(None)  
        
        if x.getLeft() == None:            
            x.setLeft(root) 
            root.recalculate_height()
            root.recalculate_balance()            
            x.recalculate_height()
            x.recalculate_balance()         
            return x
        
        elif x.getRight() == None:            
            new_root = x.getLeft()            
            new_root.setLeft(root)
            x.setLeft(None)
            new_root.setRight(x)
            x.recalculate_height()
            x.recalculate_balance()
            root.recalculate_height()
            root.recalculate_balance()
            new_root.recalculate_height()
            new_root.recalculate_balance()
            return new_root 
        
        else:#root has left and right child.
            root.setRight(x.getLeft())
            x.setLeft(root)
            root.getRight().recalculate_height()
            root.getRight().recalculate_balance()
            root.recalculate_height()
            root.recalculate_balance()
            x.recalculate_height()
            x.recalculate_balance()            
            return x       
        
    def lookUp(self,val):
        return AVLTree.__lookUp(self.root,val)
    
    def __lookUp(node,val):
        if node == None:
            return False        
        if node.getVal()==val:
            return True
        elif val < node.getVal():
            if AVLTree.__lookUp(node.getLeft(),val):
                return True       
        elif val > node.getVal():
            if AVLTree.__lookUp(node.getRight(),val):
                return True     
        
    def insert(self,val):
        
        def __insert(root,val):            
            if root == None:
                return AVLTree.AVLNode(val)
            if val < root.getVal():
                root.setLeft(__insert(root.getLeft(),val))
                self.string = self.string+"L"
                root.recalculate_height()
                root.recalculate_balance()
                if not self.pivotFound:
                    if root.getBalance()== 2 or root.getBalance() == -2:#out of balance                      
                        self.pivotFound = True
                        
                        if root.getBalance()==-2 and self.string[-1:]=="L":
                            bad_child = root.getLeft()
                            if self.string[-2:-1]=="L":                                                                
                                return AVLTree.rotateRight(root)
                            else:#self.string[-2:-1]=="R"
                                if bad_child.getRight()!=None:
                                    bad_grand_child = bad_child.getRight()                                
                                root.setLeft(AVLTree.rotateLeft(bad_child))                                
                                return AVLTree.rotateRight(root)                           
                            
                        elif root.getBalance()==2 and self.string[-1:]=="R":
                            bad_child = root.getRight()
                            if self.string[-2:-1]=="R":                                
                                return AVLTree.rotateLeft(root)
                            else:#self.string[-2:-1]=="L"
                                if bad_child.getRight()!=None:
                                    bad_grand_child = bad_child.getRight()                                
                                root.setRight(AVLTree.rotateRight(bad_child))                                
                                return AVLTree.rotateLeft(root)                                      
                        
            else: #val > root.getVal()
                root.setRight(__insert(root.getRight(),val))
                self.string = self.string+"R"
                root.recalculate_height()
                root.recalculate_balance()
                if not self.pivotFound:
                    if root.getBalance()== 2 or root.getBalance() == -2:#out of balance                      
                        self.pivotFound = True
                        
                        if root.getBalance()==-2 and self.string[-1:]=="L":
                            bad_child = root.getLeft()
                            if self.string[-2:-1]=="L":                                             
                                return AVLTree.rotateRight(root)
                            else:#self.string[-2:-1]=="R"
                                if bad_child.getRight()!=None:
                                    bad_grand_child = bad_child.getRight()                                
                                root.setLeft(AVLTree.rotateLeft(bad_child))                               
                                return AVLTree.rotateRight(root)                            
                            
                        elif root.getBalance()==2 and self.string[-1:]=="R":
                            bad_child = root.getRight()
                            if self.string[-2:-1]=="R":                                
                                return AVLTree.rotateLeft(root)
                            else:#self.string[-2:-1]=="L"
                                if bad_child.getRight()!=None:
                                    bad_grand_child = bad_child.getRight()                                
                                root.setRight(AVLTree.rotateRight(bad_child))                                
                                return AVLTree.rotateLeft(root)                                             
            return root           
        if self.lookUp(val):
            return
        self.pivotFound = False
        self.string = ""
        self.root = __insert(self.root,val)
        
    def __repr__(self):
        return "AVLTree("+repr(self.root)+")"    
    
def main():
    avl_tree = AVLTree()  
    for x in range(1000):            
        val = int((random.random()*10000000000000)%10000)        
        avl_tree.insert(val)
        if not avl_tree.root.check():#if not balanced
            print(avl_tree)   

if __name__ == '__main__':
    main()