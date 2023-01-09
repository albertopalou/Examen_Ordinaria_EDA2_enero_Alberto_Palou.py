from collections import Counter

class NodeTree(object):
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right

    def mensaje(self):
        return self.left, self.right

    def __str__(self):
        return self.left, self.right
    
def huffman_code_tree(node, binString = ""):
        if type(node) is str:
            return {node: binString}
        (l, r) = node.mensaje()
        d = dict()
        d.update(huffman_code_tree(l, binString + "0"))
        d.update(huffman_code_tree(r, binString + "1"))
        return d
    
def make_tree(nodes):
        while len(nodes) > 1:
            (key1, c1) = nodes[-1]
            (key2, c2) = nodes[-2]
            nodes = nodes[:-2]
            node = NodeTree(key1, key2)
            nodes.append((node, c1 + c2))
            nodes = sorted(nodes, key = lambda x: x[1], reverse = True)
        return nodes[0][0]

if __name__ == "__main__":
    message = "M031FA"
    key_list = ["A", "F", "1", "3", "0", "M", "T"]
    value_list = [0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]
    freq = dict(zip(key_list, value_list))
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    node = make_tree(freq)
    encoding = huffman_code_tree(node)
    for i in encoding:
        print(f"{i} : {encoding[i]}")

    

