#Largest Value in Each row
class Node(object):
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data
        
def max_level(root,arr,level):
    if (root != None):
        max_level(root.left,arr,(level + 1)) 
        if (root.val > arr[level]) :
            arr[level] = root.val
        max_level(root.right,arr,(level + 1)) 
        
def Height(root):
    if root is None:
        return 0
    lheight = Height(root.left)
    rheight = Height(root.right)
    return(max(lheight,rheight) + 1)
def main():
    root = Node(1)
    root.left = Node(3)
    root.right = Node(2)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.right = Node(9)
    arr = [-999999]*Height(root)
    max_level(root,arr,0)
    print('Max values are')
    count = 0
    for i in arr:
        print(i,end = " ")
        count += 1
        print()

if __name__ == "__main__":
    main()
