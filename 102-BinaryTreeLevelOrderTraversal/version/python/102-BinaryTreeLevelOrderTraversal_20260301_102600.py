# Last updated: 3/1/2026, 10:26:00 AM
'''
Used BFS, a queue more specifically a deque (double sided queue) for O(1) operations, then I stored the root inside the queue.

Used a while loop to calculate the length of the queue

Used a for loop to iterate through the length of the queue and adding the values to the result

Used a final for loop to search for children, if their value isn't null then they're added to the end of the queue.
'''

1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if not root:
10            return []
11        res = [] #creating an array to store our result
12        queue = deque([root]) #creating a queue more specifically a deque since it has O(1) operations since its a double sided queue and we then store the root of our tree inside of this deque
13        while len(queue) > 0: #while there are still elements in our queue
14            n = len(queue) 
15            new_level = [] #storing the values of the current level we're iterating through
16            for i in range(n): #iterating through the length of our queue
17                node = queue.popleft() #removing from our queue FIFO
18                new_level.append(node.val) #We take the value and put it into our new_level array
19                for child in [node.left, node.right]: #we then check if there are children of this node
20                    if child is not None: #if the children's value is available
21                        queue.append(child) #add the children to the end of our queue
22            res.append(new_level) #add the values of our new level array into our result array
23        return res #return our result array