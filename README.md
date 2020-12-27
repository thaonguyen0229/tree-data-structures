# Tree Data Structure
- Implementation of AVL tree and B tree (2,4 tree) in Python
## Testing program
- File **testing.py** is an executable interactive program for simple visualization of AVL tree and B tree
- Make sure **AVL.py** and **BTree.py** are in the same directory as **testing.py** before execution
### Examples
Choose AVL tree or B Tree:
```
Enter AVL or BTree: AVL
```
Enter the root (first) value:
```
Enter AVL or BTree: AVL
Enter an integer value: 1
---------------------------
Tree Structure:
- 1
Inorder Traversal: 
1
---------------------------
Enter an integer or X to quit:
```
Adding more values:
```
Enter an integer or X to quit: 55
---------------------------
Tree Structure:
- 1
  `- 55
Inorder Traversal: 
1, 55
---------------------------
Enter an integer or X to quit: 11
---------------------------
Tree Structure:
- 11
  |- 1
  `- 55
Inorder Traversal: 
1, 11, 55
---------------------------
Enter an integer or X to quit:
```
An example of B Tree:
```
Enter an integer or X to quit: 44
---------------------------
Tree Structure:
-       [3, 22, 44]
Inorder Traversal: 
3, 22, 44
---------------------------
Enter an integer or X to quit: 12
---------------------------
Tree Structure:
-       [12]
                |-      [3]
                `-      [22, 44]
Inorder Traversal: 
3, 12, 22, 44
---------------------------
Enter an integer or X to quit: 45
---------------------------
Tree Structure:
-       [12]
                |-      [3]
                `-      [22, 44, 45]
Inorder Traversal: 
3, 12, 22, 44, 45
---------------------------
Enter an integer or X to quit:
```
