from tree import *


def to_node(struct) -> INode:
    if isinstance(struct, dict):
        node = DictNode()
        for k, v in struct.items():
            node.add_node(k, to_node(v))

        return node

    if isinstance(struct, list):
        node = ListNode()
        for v in struct:
            node.add_node(to_node(v))

        return node

    return PrimitiveNode(struct)
