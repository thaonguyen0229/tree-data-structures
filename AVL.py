class AVL:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def inorder(self):
        leftS= '' if self.left == None else self.left.inorder() + ', '
        rightS = '' if self.right == None else ', ' + self.right.inorder()
        return leftS + str(self.value) + rightS

    def __str__(self):
        result = "- " + str(self.value)
        if self.left != None:
            leftS = str(self.left)
            result += "\n  |"
            for s in leftS:
                result += s
                if s == '\n': result += "  |"

        if self.right != None:
            rightS = str(self.right)
            result += "\n  "
            if self.left == None: result += "|"
            else: result += "`"
            for s in rightS:
                result += s
                if s == '\n': result += "   "
        return result




    def delete(self, value):
        self.deleteValue(value)
        self.balance()
    

    def insert(self,value):
        self.insertValue(value)
        self.balance()
    #------------------------HELPER METHODS---------------

    def balance(self):
        if self.isLeaf(): return
        bf = self.getBalanceFactor()
        if bf == -2:
            lbf = self.left.getBalanceFactor()
            if lbf == 0 or lbf == -1:self.ll_rotation()
            elif lbf == 1: self.lr_rotation()
            else:
                self.left.balance()
            return
        if bf == 2:
            rbf = self.right.getBalanceFactor()
            if rbf == 0 or rbf == 1: self.rr_rotation()
            elif rbf == -1: self.rl_rotation()
            else:
                self.right.balance()
            return
        if self.left != None:
            self.left.balance()
        if self.right != None:
            self.right.balance()

    def ll_rotation(self):
        a = self.value
        b = self.left.value
        t1 = self.left.left
        t2 = self.left.right
        if self.right != None:
            t3 = AVL(self.right.value)
            t3.left = self.right.left
            t3.right = self.right.right
        else: 
            t3 = None
            self.right = AVL(a)
        self.value = b
        self.right.value = a
        self.right.right = t3
        self.right.left = t2
        self.left = t1 

    def rr_rotation(self):     
        a = self.value
        b = self.right.value
        t1 = self.right.right
        t2 = self.right.left
        if self.left != None: # copy the tree into t3
            t3 = AVL(self.left.value)
            t3.left = self.left.left
            t3.right = self.left.right
        else: 
            t3 = None
            self.left = AVL(a)
        self.value = b
        self.left.value = a
        self.left.left = t3
        self.left.right = t2
        self.right = t1
    
    def insertValue(self, value):
        if value == self.value: return
        if value < self.value and self.left == None:
            self.left = AVL(value)
        elif value < self.value:
            self.left.insert(value)
        elif value > self.value and self.right == None:
            self.right = AVL(value)
        else:
            self.right.insert(value)
           
    def lr_rotation(self):
        a = self.value
        c = self.left.right.value
        t2 = self.left.right.left
        t3 = self.left.right.right
        if self.right != None:
            t4 = AVL(self.right.value)
            t4.left = self.right.left
            t4.right = self.right.right
        else: 
            t4 = None
            self.right = AVL(a)
        self.value = c
        self.right.value = a
        self.left.right = t2
        self.right.left = t3
        self.right.right = t4

    def rl_rotation(self):
        a = self.value
        c = self.right.left.value
        t2 = self.right.left.left
        t3 = self.right.left.right
        if self.left != None:
            t1 = AVL(self.left.value)
            t1.left = self.left.left
            t1.right = self.left.right
        else: 
            t1 = None
            self.left = AVL(a)
        self.value = c
        self.left.value = a
        self.left.left = t1
        self.left.right = t2
        self.right.left = t3

    def deleteValue(self, value):
        if self.value == value: #at the root:
            n = AVL(self.value + 1)
            n.left = self
            n.deleteValue(value)

        if self.left != None and self.left.value == value:
            if self.left.isLeaf():
                self.left = None
                
            elif self.left.right == None:
                self.left = self.left.left
            elif self.left.left == None or self.left.right.isLeaf():
                self.left.value = self.left.right.value
                self.left.right = None
            else:
                v = self.left.right.getMinimum()
                self.left.right.deleteValue(v)
                self.left.value = v
        
        if self.right != None and self.right.value == value:
            if self.right.isLeaf():
                self.right = None
                
            elif self.right.right == None:
                self.right = self.right.left
            elif self.right.left == None or self.right.right.isLeaf():
                self.right.value = self.right.right.value
                self.right.right = None
            else:
                v = self.right.right.getMinimum()
                self.right.right.deleteValue(v)
                self.right.value = v


        if value < self.value and self.left != None:
            self.left.deleteValue(value)
        if value > self.value and self.right != None:
            self.right.deleteValue(value)

    def isLeaf(self):
        return self.left == None and self.right == None
    
    def getMinimum(self):
        currentVal = self
        while currentVal.left != None:
            currentVal = currentVal.left
        return currentVal.value
    
    def getHeight(self):
        lh = 0
        if self.left != None:
            lh = self.left.getHeight()
        rh = 0
        if self.right != None:
            rh = self.right.getHeight()
        return (1 + lh if lh > rh else 1 + rh)

    def getBalanceFactor(self):
        leftH = 0 if self.left == None else self.left.getHeight()
        rightH = 0 if self.right == None else self.right.getHeight()
        return rightH - leftH