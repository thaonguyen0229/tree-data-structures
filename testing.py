from AVL import AVL
from BTree import BTree
treeType = input("Enter AVL or BTree: ")
while treeType != "AVL" and treeType != "BTree":
    treeType = input("Enter AVL or BTree: ")

value = input("Enter an integer value: ")

while type(value) is not int:
    try:
        value = int(value)
    except:
        print(value, "is not an integer")
        value = input("Enter an integer value: ")

if treeType == "AVL":
    tree = AVL(value)
else:
    tree = BTree(value)

print(type(tree))
print(tree)
print(tree.inorder())

new = input("Enter an integer or X to quit: ")
while new != "X":
    try:
        new = int(new)
    except:
        print(new, "is not an integer")
        new = input("Enter an integer value: ")
        continue
    tree.insert(new)
    print(tree)
    print(tree.inorder())
    new = input("Enter an integer or X to quit: ")

