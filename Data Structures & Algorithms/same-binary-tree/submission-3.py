# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l = deque()
        k = deque()
        l.append(p)
        k.append(q)
        if not p and not q:
            return True
        elif not p or not q:
            return False
        while k and l:
            node1 = l.popleft()
            node2 = k.popleft()
            if node1.val != node2.val:
                return False
            else:
                if node1.left and node2.left:
                    l.append(node1.left)
                    k.append(node2.left)
                elif node1.left or node2.left:
                    return False
                if node1.right and node2.right:
                    l.append(node1.right)
                    k.append(node2.right)
                elif node1.right or node2.right:
                    return False
        return True
