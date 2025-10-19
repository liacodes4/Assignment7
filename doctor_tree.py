class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None



class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, child_name, side):
        parent_node = self._find(self.root, parent_name)
        if not parent_node:
            print(f"Parent '{parent_name}' not found.")
            return
        new_node = DoctorNode(child_name)
        if side == "left":
            if parent_node.left is None:
                parent_node.left = new_node
            else:
                print(f"Left child of '{parent_name}' already exists.")
        elif side == "right":
            if parent_node.right is None:
                parent_node.right = new_node
            else:
                print(f"Right child of '{parent_name}' already exists.")
        else:
            print("Side must be 'left' or 'right'.")

    def _find(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        left_search = self._find(node.left, name)
        if left_search:
            return left_search
        return self._find(node.right, name)

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]




# Test your DoctorTree and DoctorNode classes here
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print(tree.preorder(tree.root))  # ["Dr. Croft", "Dr. Phan", "Dr. Morgan", "Dr. Carson", "Dr. Goldsmith"]
    print(tree.inorder(tree.root))   # ["Dr. Morgan", "Dr. Phan", "Dr. Carson", "Dr. Croft", "Dr. Goldsmith"]
    print(tree.postorder(tree.root)) # ["Dr. Morgan", "Dr. Carson", "Dr. Phan", "Dr. Goldsmith", "Dr. Croft"]



#Memo
#A tree works really well for the doctor structure because it clearly shows who reports to whom.
#Each doctor is a node, and their left and right children represent their direct reports. 
#This makes it easy to see the hierarchy, add new doctors, or find someone without searching through unrelated data. 
#It matches how real teams are organized.
#Traversal methods like preorder, inorder, and postorder are useful depending on the task.
#Preorder is good if we want to start with a doctor and then visit their reports, like sending information from the top down. 
#Inorder can give a “sorted” view, which is helpful for generating lists. 
#Postorder is useful if we need to handle all reports before the main doctor, such as calculating team stats or summaries.
#Heaps are perfect for emergency rooms because they automatically keep the most urgent patients at the top. 
#A min-heap ensures the patient with the lowest urgency number (the most critical) is served first. 
#When new patients arrive, the heap quickly reorganizes so priorities are always correct. 
#This simulates real-time decision-making in an ER, where acting quickly and serving the most critical patients first is essential.