class Tree:
    def __init__(self, node):
        self._node = node
        self._child = []

    def addChild(self, child):
        if isinstance(child, list):
            for node in child:
                self._child.append(Tree(node))
        else:
            self._child.append(Tree(child))

    def getNodes(self):
        return self._node

    def getChild(self):
        return self._child

    def prefixe(self, node, function):
        function(node._node)
        for n in node._child:
            node.prefixe(n, function)

    def sufixe(self, node, function):
        for n in node._child:
            node.sufixe(n, function)
        function(node._node)


if __name__ == "__main__":
    p = Tree(0)

    p.addChild([1, 8])
    p.getChild()[0].addChild([2, 4])
    p.getChild()[0].getChild()[0].addChild(3)
    p.getChild()[0].getChild()[1].addChild([5, 6])
    p.getChild()[0].getChild()[1].getChild()[1].addChild(7)

    p.getChild()[1].addChild([9, 13])
    p.getChild()[1].getChild()[0].addChild(10)
    p.getChild()[1].getChild()[0].getChild()[0].addChild([11, 12])
    p.getChild()[1].getChild()[1].addChild([14, 15])

    p.prefixe(p, print)
