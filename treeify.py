from tree import *


def treeify(struct) -> INode:
    if isinstance(struct, dict):
        node = DictNode()
        for k, v in struct.items():
            node.add_node(k, treeify(v))

        return node

    if isinstance(struct, list):
        node = ListNode()
        for v in struct:
            node.add_node(treeify(v))

        return node

    return PrimitiveNode(struct)
