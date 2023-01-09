from collections import Counter

class NodeTree(object):
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right

    def __str__(self):
        return self.left, self.right

