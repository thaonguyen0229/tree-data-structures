class BTree:
    def __init__(self, value, parent=None):
        self.keys=[value]
        self.children=[None,None]
        self.parent=parent #parent is None or a Node

    def __str__(self):
        
        result = ""
        for i in range(0, len(self.keys)):
            if self.children[i] != None:
                result += str(self.children[i]) + ", "
            result += str(self.keys[i]) + ", "

        if self.children[-1] != None:
            result += str(self.children[-1])
        else: result = result[0: len(result) - 2]

        if self.parent == None:
            result = "B tree has " + str(self.getSize()) + " elements:\n" + result
        return result

    def insert(self, value):
        if self.isExternal():
            i = 0
            for k in self.keys:
                if value == k: return
                if value > k: i += 1
            self.keys.insert(i, value)
            if self.children[i] == None or self.children[i].keys[0] > value:
                self.children.insert(i, None)
            else:
                self.children.insert(i+1, None)

        else:
            for i in range(0, len(self.keys)):
                if value == self.keys[i]: return

                if value < self.keys[i]: #and self.children[i] != None:
                    self.children[i].insert(value)

                #elif value < self.keys[i]:
                 #   self.children[i] = BTree(value, self)
                
            if value > self.keys[-1]: #and self.children[-1] != None:
                self.children[-1].insert(value)
            #elif value > self.keys[-1]:
             #   self.children[-1] = BTree(value, self)
        
        self.overflowAndsplit() # check and handle overflow
        

    def delete(self, value):
        if self.isExternal() and not value in self.keys: return

        if value > self.keys[-1]:
            self.children[-1].delete(value)

        for i in range(len(self.keys)):
            if value == self.keys[i] and self.isExternal():
                self.keys.pop(i)
                if len(self.keys) > 0: self.children.remove(None)
                else: self.underflow()
                break
            elif value == self.keys[i]:
                self.keys.pop(i)
                self.transfer(i)
                break
            elif value < self.keys[i]:
                self.children[i].delete(value)
                break
        
    #-----------------HELPER METHODS----------------
    def transfer(self, index):
        if self.isExternal():
            if len(self.keys) > 0 : self.children.remove(None)
            else: self.underflow()
            return
        self.keys.insert(index, self.children[index+1].keys[0]) # always transfer from right child
        self.children[index+1].keys = self.children[index+1].keys[1:]
        self.children[index+1].transfer(0)


    def isExternal(self):
        for c in self.children:
            if c != None : return False
        return True

    def getSize(self):
        if self.isExternal(): return len(self.keys)
        count = 0
        for i in self.children:
            count += i.getSize()
        return len(self.keys) + count

    # Check and handle overflow
    def overflowAndsplit(self):
        if len(self.keys) <= 3: return
        # Overflow at the root
        if self.parent == None:
            newK = [self.keys[1]]
            newC = [BTree(self.keys[0], self), BTree(self.keys[2], self)]
            newC[1].keys.append(self.keys[3])
            newC[0].children = self.children[0:2]
            newC[1].children = self.children[2:]
            if not self.isExternal():
                self.children[0].parent = newC[0]
                self.children[1].parent = newC[0]
                for i in range(2, len(self.children)):
                    self.children[i].parent = newC[1]
            self.keys = newK
            self.children = newC
        
        # Overflow at internal node
        else: # insert self.keys[2] into the parent
            leftC = BTree(self.keys[0], self.parent)
            leftC.keys.append(self.keys[1])
            leftC.children = self.children[0:3]

            rightC = BTree(self.keys[3], self.parent)
            rightC.children = self.children[3:]

            i = 0
            for k in self.parent.keys:
                if self.keys[2] > k: i +=1
            
            self.parent.keys.insert(i, self.keys[2])
            self.parent.children[i] = leftC
            self.parent.children.insert(i+1, rightC)
            rightC.parent.overflowAndsplit()


    # check and handle underflow
    def underflow(self):
        parent = self.parent
        index = 0
        for i in range(len(parent.children)):
            if len(parent.children[i].keys) == 0:
                index = i
                break       
        #transfer from 3-node or 4-node sibling
        for s in range(len(parent.children)):
            if index == s: continue
            sibling = parent.children[s]
            if len(sibling.keys) > 1 and s < index: #sibling in front
                if len(parent.keys) == index: index = -1
                self.keys.append(parent.keys[index])
                parent.keys.pop(index)
                parent.keys.insert(s, sibling.keys[-1])
                sibling.keys.pop()
                sibling.children.pop()
                return
            elif len(sibling.keys) > 1: #sibling behind
                self.keys.append(parent.keys[index])
                parent.keys.pop(index)
                parent.keys.insert(s, sibling.keys[0])
                sibling.keys.pop(0)
                sibling.children.pop(0)
                return
        
        # fusion: all siblings are 2-node, fusion with adjacent sibling
        s = 1 if index == 0 else index - 1
        parent.children[s].keys.append(parent.keys[s])
        parent.keys.pop(s)
        parent.children.pop(index)
        parent.children[s].children.append(None)