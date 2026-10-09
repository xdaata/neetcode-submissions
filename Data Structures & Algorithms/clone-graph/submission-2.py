"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        clones = {}

        def dfs(old_node):
            if old_node in clones:
                return clones[old_node]

            new_node = Node(old_node.val)
            clones[old_node] = new_node

            for neigh in old_node.neighbors:
                new_node.neighbors.append(dfs(neigh))
            
            return new_node
        
        return dfs(node)